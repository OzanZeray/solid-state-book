# Chapter 15: Optical Processes and Excitons

## Dielectric Function of Semiconductors

The complex dielectric function epsilon(omega) = epsilon_1 + i*epsilon_2 encodes all linear optical response. Aspnes and Studna (1983) performed spectroscopic ellipsometry on Si and Ge, providing the standard reference data used in semiconductor optics.

> "We report pseudodielectric function spectra <epsilon(omega)> for Si, Ge, GaP, GaAs, GaSb, InP, InAs, and InSb from 1.5 to 6.0 eV." -- Aspnes & Studna, Phys. Rev. B 27, 985 (1983)

| Material | E_1 critical point (eV) | E_2 critical point (eV) | epsilon_1 at 2 eV | epsilon_2 at 4.3 eV |
|----------|------------------------|------------------------|-------------------|---------------------|
| Si       | 3.4                    | 4.25                   | 15.3              | 38.5                |
| Ge       | 2.1                    | 4.35                   | 21.6              | 29.7                |
| GaAs     | 2.9                    | 4.7                    | 12.0              | 26.8                |
| GaP      | 3.7                    | 5.3                    | 10.2              | 18.1                |
| InP      | 3.2                    | 4.7                    | 11.4              | 20.0                |

The critical-point structure in epsilon_2 directly maps the joint density of states at van Hove singularities in the band structure.

## Raman Scattering in Diamond

Raman spectroscopy probes zone-center optical phonons. Diamond has a single first-order Raman-active mode (T_2g symmetry). Liu et al. (2000) studied the diamond Raman line under high pressure.

> "The zone-center optical phonon frequency of diamond at ambient conditions is 1332.5 cm^-1." -- Liu et al., Phys. Rev. B 61, 3391 (2000)

| Material      | Raman frequency (cm^-1) | Symmetry | Linewidth (cm^-1) |
|---------------|------------------------|----------|-------------------|
| Diamond       | 1332.5                 | T_2g     | 1.2               |
| Si            | 520.7                  | T_2g     | 3.5               |
| Ge            | 300.7                  | T_2g     | 3.2               |
| GaAs (LO)     | 292                    | --       | 3.0               |
| GaAs (TO)     | 269                    | --       | 2.5               |
| 6H-SiC (A_1) | 967                    | A_1(LO)  | 2.8               |

The narrow linewidth of diamond (1.2 cm^-1) reflects its exceptionally long phonon lifetime due to limited anharmonic decay channels.

## Excitons: Wannier and Frenkel Types

Excitons are bound electron-hole pairs. In semiconductors with large dielectric constants, the Wannier exciton binding energy follows a hydrogen-like series: E_n = -E_x / n^2.

| Material | Exciton binding energy E_x (meV) | Bohr radius a_x (nm) | Type    |
|----------|----------------------------------|----------------------|---------|
| GaAs     | 4.2                             | 13                   | Wannier |
| CdS      | 28                              | 2.8                  | Wannier |
| ZnO      | 60                              | 1.8                  | Wannier |
| Cu2O     | 97                              | 1.1                  | Wannier |
| NaCl     | ~1000                           | ~0.3                 | Frenkel |
| Anthracene| ~1000                           | ~0.5                 | Frenkel |

## Giant Rydberg Excitons in Cu2O

Kazimierczuk et al. (2014) observed Rydberg exciton states in Cu2O up to principal quantum number n = 25, a landmark achievement in semiconductor spectroscopy.

> "Here we observe giant Rydberg excitons with principal quantum numbers as large as n = 25 in cuprous oxide... the coherence of these exciton states is remarkable." -- Kazimierczuk et al., Nature 514, 343 (2014)

Selected absorption peak positions from the yellow exciton series in Cu2O at 1.2 K:

| n  | Energy (eV)  | Linewidth (micro-eV) |
|----|-------------|----------------------|
| 2  | 2.1478      | --                   |
| 5  | 2.1680      | 150                  |
| 10 | 2.1710      | 40                   |
| 15 | 2.1718      | 20                   |
| 20 | 2.1721      | 12                   |
| 25 | 2.1723      | 8                    |

The series converges to the band gap at 2.17208 eV. The exciton size at n = 25 exceeds 1 micrometer, making it a mesoscopic quantum object. Rydberg blockade effects were observed at high densities.

## Optical Absorption Edge

The absorption coefficient alpha near the band edge distinguishes direct and indirect gap semiconductors:
- Direct gap: alpha ~ (h*nu - E_g)^(1/2)
- Indirect gap: alpha ~ (h*nu - E_g +/- E_phonon)^2

| Material | Band gap (eV) | Gap type  | alpha at E_g + 0.1 eV (cm^-1) |
|----------|---------------|-----------|-------------------------------|
| GaAs     | 1.42          | Direct    | ~8000                         |
| InP      | 1.34          | Direct    | ~5000                         |
| Si       | 1.12          | Indirect  | ~50                           |
| Ge       | 0.66          | Indirect  | ~300                          |
| GaN      | 3.39          | Direct    | ~10^5                         |

The sharp onset in direct-gap materials makes them ideal for optoelectronic devices.

## References

1. D. E. Aspnes and A. A. Studna, "Dielectric functions and optical parameters of Si, Ge, GaP, GaAs, GaSb, InP, InAs, and InSb from 1.5 to 6.0 eV," Phys. Rev. B **27**, 985 (1983). DOI: [10.1103/PhysRevB.27.985](https://doi.org/10.1103/PhysRevB.27.985)
2. T. Kazimierczuk et al., "Giant Rydberg excitons in the copper oxide Cu2O," Nature **514**, 343 (2014). DOI: [10.1038/nature13832](https://doi.org/10.1038/nature13832)
3. L. Liu et al., "High-pressure Raman study of diamond," Phys. Rev. B **61**, 3391 (2000). DOI: [10.1103/PhysRevB.61.3391](https://doi.org/10.1103/PhysRevB.61.3391)
4. R. J. Elliott, "Intensity of Optical Absorption by Excitons," Phys. Rev. **108**, 1384 (1957). DOI: [10.1103/PhysRev.108.1384](https://doi.org/10.1103/PhysRev.108.1384)
5. P. Y. Yu and M. Cardona, *Fundamentals of Semiconductors*, 4th ed. (Springer, 2010).
