# ComPACT
[![arXiv:2309.17077](http://img.shields.io/badge/arXiv-2309.17077-B31B1B.svg)](https://arxiv.org/abs/2309.17077) [<img src="https://cds.unistra.fr/img/cds/vizier.svg" width="50" height="30">](https://cdsarc.cds.unistra.fr/viz-bin/cat/J/MNRAS/531/1998)

The catalogue was created based on the extended candidate catalogue of the Planck clusters ([SZcat](https://github.com/astromining/planck_szcat)) and deep learning algorithm, that was trained on the ACT+Planck maps ([Naess et al. 2020](https://iopscience.iop.org/article/10.1088/1475-7516/2020/12/046)). 


The ComPACT catalogue contains 2,962 candidates. Below we describe columns:
| Column | Description | Units / Notes |
| :--- | :--- | :--- |
| **Name**     | ID of a ComPACT candidate | Unique identifier |
| **RA**       | Right Ascension of maximum pixel | Decimal degrees (J2000) |
| **DEC**      | Declination of maximum pixel | Decimal degrees (J2000) |
| **S**        | Object mask area | Pixels |
| **pmax**     | Maximum probability for an object | Probability score [0, 1] |
| **SZcat**    | Name of the object from SZcat catalogue | Cross-match ID |
| **ACT**      | Cluster name in the ACT DR5 catalogue | Cross-match ID |
| **PSZ2**     | PSZ2 source name | Cross-match ID |
| **Priority** | Reliability of candidate based on $S$ area | See levels below |

### Priority Levels
The `Priority` column indicates the reliability of the candidate based on the mask area ($S$), corresponding to different purity levels:

| Priority | Condition ($S$) | Minimum Purity ($Purity_{min}$) | Reliability |
| :---: | :--- | :---: | :--- |
| **1** | $S > 30$ | $0.84$ | Highest |
| **2** | $S > 25$ | $0.78$ | High |
| **3** | $S > 20$ | $0.74$ | Moderate |

For columns we used catalogues:
+ SZcatgen: [data](https://github.com/astromining/planck_szcat), [Meshcheryakov et al. 2022](https://link.springer.com/article/10.1134/S1063773722090055)
+ ACT DR5: [data](https://lambda.gsfc.nasa.gov/product/act/actpol_dr5_szcluster_catalog_get.html), [Hilton et al. 2021](https://iopscience.iop.org/article/10.3847/1538-4365/abd023)
+ PSZ2: [data](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=J/A%2bA/594/A27/psz2&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa), [Planck Collobaration](https://ui.adsabs.harvard.edu/abs/2016A%26A...594A..27P/abstract)


## ComPACT pipeline

This section describes how to reproduce the ComPACT cluster detection workflow using the [galaxyHackers](https://github.com/astromining/galaxyHackers):

### ▶ Quick Start

1. **Train / Run inference**  
   ```bash
   python3 -m galaxy.main --models CNN_MLP --epochs 50 --data ACT
   ```

2. **To build full-sky segmentation map**  
   ```bash
    python3 -m galaxy.full_sky start --checkpoint /abs/path/to/checkpoint.pth --model CNN_MLP --optimizer AdamW --data ACT
   ```
   - Replace `/abs/path/to/checkpoint.pth` with your trained model path

Full description see on the [galaxyHackers github](https://github.com/astromining/galaxyHackers)

---

## Version History

Cluster calalogue: ComPACT.csv (v2.0)
+ v2.0 Add 'Priority' column, which is responsible for subsamples with different purity and completeness characteristics. Also, We keep the nearest object in 5 arcmin window (before all objects in 5 arcmin window). Also, now we cross-match objects from full catalogue with SZcat, before we crop 5 arcmin window from probability map and analyse groups
+ v1.1 Negative RA coordinates in catalog are fixed (e.g -152.41666 -> 207.58333)
+ v1.0 Initial release (in folder v1.0)

-----

**Bibcode:** [2024MNRAS.531.1998V (ADS)](https://ui.adsabs.harvard.edu/abs/2024MNRAS.531.1998V)

**Vizier:** [ComPACT, ACT+Planck galaxy cluster cat. : J/MNRAS/531/1998](https://cdsarc.cds.unistra.fr/viz-bin/cat/J/MNRAS/531/1998)

**arXiv:** [arXiv:2309.17077](https://arxiv.org/abs/2309.17077)

