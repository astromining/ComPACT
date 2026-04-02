import torch
from torch import nn

class ConvBlock(nn.Module):
    def __init__(self, in_size, out_size, kernel_size=3, padding=1, stride=1, bias=False):
        super(ConvBlock, self).__init__()
        self.conv = nn.Conv2d(
            in_size, 
            out_size, 
            kernel_size, 
            padding=padding, 
            stride=stride,
            bias=bias
        )
        self.bn = nn.BatchNorm2d(out_size)
        self.nonr = nn.ReLU(inplace=True)

    def forward(self, x):
        return self.nonr(self.bn(self.conv(x)))
    
class Classification(nn.Module):
    def __init__(self, p=0.5, sizes_conv = [3, 16, 32, 64, 128], 
                 sizes = [512, 256, 128, 1]):
        super(Classification, self).__init__()
        self.sizes = sizes
        self.sizes_conv = sizes_conv
        kernel_ = [5, 3, 3, 3, 3]
        
        layers = []
        for i in range(1, len(sizes_conv)):
            layers.append(ConvBlock(self.sizes_conv[i-1], self.sizes_conv[i], kernel_size=kernel_[i], stride=1, padding=1, bias=False))
            layers.append(ConvBlock(self.sizes_conv[i], self.sizes_conv[i], kernel_size=3, stride=1, padding=1, bias=False))
            layers.append(nn.MaxPool2d(2, 2),)
        
        layers.append(nn.Flatten())

        for i in range(1, len(sizes)-1):
            if i > 1:
                layers.append(nn.ReLU(inplace=True))
                layers.append(nn.Dropout(p))
            layers.append(nn.Linear(self.sizes[i-1], self.sizes[i], bias=False))
            layers.append(nn.BatchNorm1d(self.sizes[i]))
        layers.append(nn.ReLU(inplace=True))
        layers.append(nn.Dropout(p))
        self.layers = nn.Sequential(*layers)

        
        self.out = nn.Linear(self.sizes[-2], self.sizes[-1])
        self.init_weights(self.out)
        self.layers.apply(self.init_weights)


    def forward(self, x1, x2, x3):
        x = torch.cat([x1, x2, x3], 1)
        x = self.layers(x)
        x = self.out(x)
        x = torch.sigmoid(x)

        return x
    
    def init_weights(self, x):
        if isinstance(x, nn.Linear):
            torch.nn.init.kaiming_uniform_(x.weight, nonlinearity='relu')
