# ComPACT
[![arXiv:2309.17077](http://img.shields.io/badge/arXiv-2309.17077-B31B1B.svg)](https://arxiv.org/abs/2309.17077) [<img src="https://cds.unistra.fr/img/cds/vizier.svg" width="50" height="30">](https://cdsarc.cds.unistra.fr/viz-bin/cat/J/MNRAS/531/1998)

The catalogue was created based on the extended candidate catalogue of the Planck clusters ([SZcat](https://github.com/astromining/planck_szcat)) and deep learning algorithm, that was trained on the ACT+Planck maps ([Naess et al. 2020](https://iopscience.iop.org/article/10.1088/1475-7516/2020/12/046)). 

The ComPACT catalogue contains 2,962 candidates. Below we describe columns:

### Basic Properties & Cross-matches 

| Column | Description | Units / Notes |
| :--- | :--- | :--- |
| **Name** | ID of a ComPACT candidate | Unique identifier |
| **RA** | Right Ascension of maximum pixel | Decimal degrees (J2000) |
| **DEC** | Declination of maximum pixel | Decimal degrees (J2000) |
| **S** | Object mask area | Pixels |
| **pmax** | Maximum probability for an object | Probability score [0, 1] |
| **SZcat** | Name of the object from SZcat catalogue | Cross-match ID* |
| **ACT** | Cluster name in the ACT DR5 catalogue | Cross-match ID* |
| **PSZ2** | PSZ2 source name | Cross-match ID* |
| **Priority** | Reliability of candidate based on $S$ area | See levels descriprion in arxiv_2309.17077 folder |

*file with this columns in folder arXiv_2309.17077

### Redshift and Mass Parameters (v3.0)

| Column | Description | Units / Notes |
| :--- | :--- | :--- |
| **z** | Cluster redshift |  |
| **zType** | Redshift type | `spec` (spectroscopic) or `phot` (photometric) |
| **zSource** | Source of the cluster redshift | Reference ID (see *Data Sources*) |
| **zCluster_delta** | `zCluster` density contrast statistic | see [zCluster](https://github.com/ACTCollaboration/zCluster) |
| **zCluster_err** | Uncertainty in `zCluster_delta` |  |
| **zZazn_sig1** | `Zaznobin` first significance value | Significance ($p_1$) (see [Zaznobin git](https://github.com/izaznobin/zPhot_Zaznobin)) |
| **zZazn_sig2** | `Zaznobin` second significance value | Significance ($p_2$) (see [Zaznobin git](https://github.com/izaznobin/zPhot_Zaznobin)) |
| **zZazn_err** | Uncertainty in `Zaznobin` redshift |  |
| **M500** | Cluster mass ($M_{500c}$) | $10^{14} \, M_\odot$; asymmetric uncertainties: `E_M500` (upper), `e_M500` (lower) |
| **mSource** | Source of the mass estimate | Reference ID (see *Data Sources*)|
| **Mact** | Mass from $Y$–$M$ relation (ACT+Planck $y$-maps) | $10^{14} \, M_\odot$; uncertainties: `e_Mact`, `E_Mact` |
| **Mplanck** | Mass from $Y$–$M$ relation (Planck-only $y$-maps) | $10^{14} \, M_\odot$; uncertainties: `e_Mplanck`, `E_Mplanck` |

---
## Data Sources & References
For columns we used catalogues:
+ SZcatgen: [data](https://github.com/astromining/planck_szcat), [Meshcheryakov et al. 2022](https://link.springer.com/article/10.1134/S1063773722090055)
+ ACT DR5: [data](https://lambda.gsfc.nasa.gov/product/act/actpol_dr5_szcluster_catalog_get.html), [Hilton et al. 2021](https://iopscience.iop.org/article/10.3847/1538-4365/abd023)
+ PSZ2: [data](https://vizier.cds.unistra.fr/viz-bin/VizieR-3?-source=J/A%2bA/594/A27/psz2&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa), [Planck Collobaration](https://ui.adsabs.harvard.edu/abs/2016A%26A...594A..27P/abstract)
+ zCluster: [github](https://github.com/ACTCollaboration/zCluster), [Hilton et al. 2018](https://ui.adsabs.harvard.edu/abs/2018ApJS..235...20H/abstract)
+ Zaznobin algorithm: [github](https://github.com/izaznobin/zPhot_Zaznobin), [Zaznobin et al. 2023](https://ui.adsabs.harvard.edu/abs/2023AstL...49..431Z/abstract)
+ Redshift/Mass Sources: Detailed references for specific `zSource` and `mSource` IDs are provided in the Table 1 of the v3.0 paper.

---

## Version History
Cluster calalogue: ComPACT.csv (v2.0)
+ v3.0 Measure mass and readshifts. Released accompanying paper:
+ v2.0 Add 'Priority' column, which is responsible for subsamples with different purity and completeness characteristics. Also, We keep the nearest object in 5 arcmin window (before all objects in 5 arcmin window). Also, now we cross-match objects from full catalogue with SZcat, before we crop 5 arcmin window from probability map and analyse groups
+ v1.1 Negative RA coordinates in catalog are fixed (e.g -152.41666 -> 207.58333)
+ v1.0 Initial release (in folder v1.0)

-----

## Links & Citations

### Main Paper (v2.0)
*   **Bibcode:** [2024MNRAS.531.1998V (ADS)](https://ui.adsabs.harvard.edu/abs/2024MNRAS.531.1998V)
*   **arXiv:** [arXiv:2309.17077](https://arxiv.org/abs/2309.17077v3)

### New Paper (v3.0 - Masses & Redshifts)
*   **Bibcode:** 
*   **arXiv:** 

### Data Archives
*   **Vizier:** [ComPACT: J/MNRAS/531/1998](https://cdsarc.cds.unistra.fr/viz-bin/cat/J/MNRAS/531/1998)