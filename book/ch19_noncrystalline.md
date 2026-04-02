# Chapter 19: Noncrystalline Solids

## Short-Range Order: Radial Distribution Functions

Amorphous solids lack long-range periodional order but retain short-range order characterized by the radial distribution function (RDF) g(r). Laaziri et al. (1999) performed high-resolution X-ray diffraction on amorphous silicon, providing the most precise RDF measurement.

> "The first-neighbor distance in a-Si is 2.35 +/- 0.01 A with a coordination number of 3.88 +/- 0.05, very close to the crystalline value of 4." -- Laaziri et al., Phys. Rev. B 60, 13520 (1999)

| Parameter                 | a-Si (Laaziri 1999) | c-Si (diamond) | Difference |
|--------------------------|--------------------|----|------------|
| First-neighbor distance   | 2.35 A             | 2.35 A          | < 0.01 A   |
| Coordination number       | 3.88               | 4.00            | -3%        |
| Bond angle                | 109.5 +/- 10 deg  | 109.47 deg      | ~10 deg spread |
| Second-neighbor distance  | 3.83 A             | 3.84 A          | ~0.01 A    |
| Second-neighbor width     | 0.25 A (FWHM)     | < 0.05 A        | broadened  |

The key finding: bond lengths are preserved to high accuracy; the disorder manifests primarily as bond-angle distortions.

## Vitreous SiO2 Structure

Wright (1994) compiled neutron and X-ray diffraction data for vitreous silica, the archetypal network glass.

| Structural parameter     | Vitreous SiO2      | alpha-Quartz     |
|-------------------------|--------------------|----|
| Si-O bond length         | 1.608 A            | 1.609, 1.612 A   |
| O-Si-O angle             | 109.5 deg          | 108.8-110.5 deg  |
| Si-O-Si angle            | 144 +/- 35 deg     | 143.7 deg        |
| Si coordination          | 4.0                | 4                 |
| O coordination           | 2.0                | 2                 |
| Density                  | 2.20 g/cm^3        | 2.65 g/cm^3      |

Vitreous SiO2 consists of corner-sharing SiO4 tetrahedra with a broad distribution of Si-O-Si bridging angles, producing a continuous random network (Zachariasen model).

## Glass Transition Temperatures

The glass transition temperature T_g marks the crossover from supercooled liquid to glassy solid. It depends on cooling rate but is reproducible for standard rates (~10 K/min).

| Material               | T_g (K) | T_m (K) | T_g / T_m | Type           |
|-----------------------|---------|---------|-----------|----------------|
| SiO2                   | 1473    | 1996    | 0.74      | Oxide network  |
| B2O3                   | 530     | 723     | 0.73      | Oxide network  |
| GeO2                   | 815     | 1389    | 0.59      | Oxide network  |
| Na2O-2SiO2             | 727     | 1147    | 0.63      | Modified oxide |
| Polystyrene             | 373     | ~513    | 0.73      | Polymer        |
| Glycerol               | 190     | 291     | 0.65      | Molecular      |
| Se                     | 310     | 494     | 0.63      | Chalcogenide   |
| As2S3                   | 478     | 585     | 0.82      | Chalcogenide   |
| Zr41Ti14Cu12.5Ni10Be22.5| 623    | 993     | 0.63      | Metallic (Vit1)|
| Pd40Ni40P20             | 590     | 884     | 0.67      | Metallic       |

The ratio T_g/T_m ~ 2/3 (Kauzmann's rule) holds approximately for many glass formers.

## Electronic Properties of Amorphous Semiconductors

Anderson localization in disordered systems creates a mobility edge separating extended and localized states. The density of states in a-Si:H features:

| Energy region                    | States                    | Density (cm^-3 eV^-1) |
|---------------------------------|----|----------------------|
| Conduction band (extended)       | Extended above E_c        | ~10^21               |
| Conduction band tail             | Localized, exponential    | ~10^18-10^20         |
| Mid-gap defects (dangling bonds) | Localized                 | ~10^15-10^16 (a-Si:H)|
| Valence band tail                | Localized, exponential    | ~10^18-10^20         |
| Valence band (extended)          | Extended below E_v        | ~10^21               |

Hydrogenation (a-Si:H) reduces the dangling-bond density from ~10^19 cm^-3 in pure a-Si to ~10^15-10^16 cm^-3, enabling device applications (solar cells, TFTs).

## Kauzmann Paradox and Fragility

Angell (1995) classified glass formers by their fragility -- the departure from Arrhenius viscosity behavior.

| Glass former    | Fragility index m | Classification |
|----------------|-------------------|----------------|
| SiO2            | 20                | Strong         |
| GeO2            | 20                | Strong         |
| Glycerol        | 53                | Intermediate   |
| o-Terphenyl     | 81                | Fragile        |
| PVC             | 191               | Very fragile   |

Strong liquids (SiO2) show Arrhenius viscosity; fragile liquids show dramatic super-Arrhenius slowdown near T_g.

## References

1. K. Laaziri et al., "High-resolution radial distribution function of pure amorphous silicon," Phys. Rev. B **60**, 13520 (1999). DOI: [10.1103/PhysRevB.60.13520](https://doi.org/10.1103/PhysRevB.60.13520)
2. A. C. Wright, "Neutron scattering from vitreous silica. V. The structure of vitreous silica: What have we learned from 60 years of diffraction studies?," J. Non-Cryst. Solids **179**, 84 (1994). DOI: [10.1016/0022-3093(94)90687-4](https://doi.org/10.1016/0022-3093(94)90687-4)
3. C. A. Angell, "Formation of Glasses from Liquids and Biopolymers," Science **267**, 1924 (1995). DOI: [10.1126/science.267.5206.1924](https://doi.org/10.1126/science.267.5206.1924)
4. P. W. Anderson, "Absence of Diffusion in Certain Random Lattices," Phys. Rev. **109**, 1492 (1958). DOI: [10.1103/PhysRev.109.1492](https://doi.org/10.1103/PhysRev.109.1492)
5. R. A. Street, *Hydrogenated Amorphous Silicon* (Cambridge University Press, 1991).
