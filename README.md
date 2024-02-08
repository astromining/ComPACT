# ComPACT

[![arXiv:2309.17077](http://img.shields.io/badge/arXiv-2309.17077-B31B1B.svg)](https://arxiv.org/abs/2309.17077)

The catalogue was created based on the extended candidate catalogue of the Planck clusters ([SZcat](https://github.com/astromining/planck_szcat)) and deep learning algorithm, that was trained on the ACT+Planck maps ([Naess et al. 2020](https://iopscience.iop.org/article/10.1088/1475-7516/2020/12/046)). 

The ComPACT catalogue contains 2,962 candidates. Below we describe columns:
+ Name: ID of a ComPACT candidate
+ RA: Right Ascension in decimal degrees (J2000) of maximum pixel
+ DEC: Declination in decimal degrees (J2000) of maximum pixel
+ S: Object mask area in pixels
+ pmax: Maximum probability for an object
+ SZcat: Name of the object from the SZcat catalogue
+ ACT: Cluster name in the ACT DR5 catalogue
+ PSZ2:	PSZ2 source name 
+ Priority: Priotity of candidate along S area:
  ++ 1: S > 30 (the most probable, $Purity_{min} = 0.8$)
  ++ 2: S > 25 ($Purity_{min} = 0.78$)
  ++ 3: S > 20 ($Purity_{min} = 0.74$)

For columns we used catalogues:
+ SZcatgen: [data](https://github.com/astromining/planck_szcat), [Meshcheryakov et al. 2022](https://link.springer.com/article/10.1134/S1063773722090055)
+ ACT DR5: [data](https://lambda.gsfc.nasa.gov/product/act/actpol_dr5_szcluster_catalog_get.html), [Hilton et al. 2021](https://iopscience.iop.org/article/10.3847/1538-4365/abd023)
+ PSZ2: [data](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=J/A%2bA/594/A27/psz2&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa), [Planck Collobaration](https://ui.adsabs.harvard.edu/abs/2016A%26A...594A..27P/abstract)

Description:
Cluster calalogue: ComPACT.csv (v2.0)
+ v2.0 Add 'Priority' column, which is responsible for subsamples with different purity and completeness characteristics. Also, We keep the nearest object in 5 arcmin window (before all objects in 5 arcmin window). Also, now we cross-match objects from full catalogue with SZcat, before we crop 5 arcmin window from probability map and analyse groups
+ v1.1 Negative RA coordinates in catalog are fixed (e.g -152.41666 -> 207.58333)
+ v1.0 Initial release (in folder v1.0)