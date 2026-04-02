# Chapter 14: Plasmons, Polaritons, and Polarons

## Bulk Plasmon Energy Loss in Metals

Electron energy-loss spectroscopy (EELS) provides direct measurement of bulk plasmon energies. Powell and Swan (1959) transmitted keV electrons through thin Al films and observed a dominant loss peak at 15.3 eV, confirming the free-electron plasmon prediction.

> "The energy losses observed in aluminium are 15.0 +/- 0.3 eV... in good agreement with the value 15.7 eV calculated from the free-electron formula." -- Powell & Swan, Phys. Rev. 115, 869 (1959)

| Metal | Measured plasmon energy (eV) | Free-electron prediction (eV) | Electron density n (10^28 m^-3) |
|-------|----------------------------|-------------------------------|--------------------------------|
| Al    | 15.3                       | 15.8                          | 18.1                           |
| Mg    | 10.6                       | 10.9                          | 8.61                           |
| Si    | 16.5                       | 16.0                          | --                             |
| Na    | 5.7                        | 5.9                           | 2.65                           |
| K     | 3.7                        | 4.3                           | 1.40                           |
| Be    | 18.7                       | 18.4                          | 24.7                           |

The close agreement between measured and free-electron values for simple metals validates the Drude dielectric function. Deviations in Si reflect interband transition contributions.

## Surface Plasmons

Ritchie (1957) predicted surface plasmon modes at energy omega_s = omega_p / sqrt(2). For Al, the surface plasmon appears at 10.3 eV in reflection EELS. Surface plasmons are now routinely excited by infrared light on nanostructured metal surfaces (localized surface plasmon resonance), forming the basis of plasmonic biosensors.

## Lyddane-Sachs-Teller Relation and Polaritons

The LST relation connects the static and high-frequency dielectric constants to the longitudinal and transverse optical phonon frequencies: epsilon(0)/epsilon(inf) = (omega_LO / omega_TO)^2.

| Crystal | omega_LO (cm^-1) | omega_TO (cm^-1) | epsilon(0)/epsilon(inf) measured | (omega_LO/omega_TO)^2 |
|---------|-------------------|-------------------|--------------------------------|----------------------|
| GaAs    | 292               | 269               | 1.18                           | 1.18                 |
| InSb    | 197               | 185               | 1.14                           | 1.13                 |
| NaCl    | 264               | 164               | 5.9                            | 2.59                 |
| LiF     | 659               | 307               | 8.9                            | 4.61                 |

For strongly ionic crystals (NaCl, LiF) the LO-TO splitting is large, producing a wide reststrahlen band where infrared reflectivity approaches unity.

## Polariton Dispersion

Henry and Hopfield (1965) measured the polariton dispersion in GaP using Raman scattering, demonstrating the anticrossing between photon and TO-phonon branches. The phonon-polariton gap between omega_TO and omega_LO is directly observable as a forbidden frequency region in infrared transmission.

## Polarons and the Mott Metal-Insulator Transition

The electron-phonon coupling in polar semiconductors dresses carriers as polarons. A dramatic consequence of electron-electron and electron-lattice interactions is the Mott transition. Rosenbaum et al. (1983) studied the metal-insulator transition in Si:P, finding the critical phosphorus concentration n_c = 3.74 x 10^18 cm^-3.

> "We find the transition to be continuous... the critical concentration n_c = 3.74 +/- 0.04 x 10^18 cm^-3." -- Rosenbaum et al., Phys. Rev. B 27, 7509 (1983)

| Dopant system | Critical concentration n_c (cm^-3) | Mott criterion (n_c)^(1/3) a_B |
|---------------|-----------------------------------|---------------------------------|
| Si:P          | 3.74 x 10^18                      | 0.26                            |
| Si:B          | 4.06 x 10^18                      | 0.31                            |
| Si:As         | 8.5 x 10^18                       | 0.25                            |
| Ge:Sb         | 1.2 x 10^17                       | 0.26                            |

The Mott criterion (n_c)^(1/3) a_B ~ 0.26 holds remarkably well across different host-dopant combinations.

## Polaron Effective Mass

| Material | alpha (Froehlich coupling) | m*/m_band | Method           |
|----------|---------------------------|-----------|------------------|
| InSb     | 0.014                     | 1.01      | Cyclotron res.   |
| GaAs     | 0.068                     | 1.03      | Cyclotron res.   |
| CdTe     | 0.39                      | 1.05      | Magneto-optical  |
| AgBr     | 1.53                      | 1.26      | Optical abs.     |
| SrTiO3   | 3.77                      | ~3        | Transport        |
| KCl      | 3.44                      | 2.5       | Optical abs.     |

Weak-coupling materials (alpha < 1) show small mass enhancement; strong-coupling materials approach small-polaron behavior.

## References

1. C. J. Powell and J. B. Swan, "Origin of the Characteristic Electron Energy Losses in Aluminum," Phys. Rev. **115**, 869 (1959). DOI: [10.1103/PhysRev.115.869](https://doi.org/10.1103/PhysRev.115.869)
2. T. F. Rosenbaum et al., "Metal-insulator transition in a doped semiconductor," Phys. Rev. B **27**, 7509 (1983). DOI: [10.1103/PhysRevB.27.7509](https://doi.org/10.1103/PhysRevB.27.7509)
3. R. H. Ritchie, "Plasma Losses by Fast Electrons in Thin Films," Phys. Rev. **106**, 874 (1957). DOI: [10.1103/PhysRev.106.874](https://doi.org/10.1103/PhysRev.106.874)
4. C. H. Henry and J. J. Hopfield, "Raman Scattering by Polaritons," Phys. Rev. Lett. **15**, 964 (1965). DOI: [10.1103/PhysRevLett.15.964](https://doi.org/10.1103/PhysRevLett.15.964)
5. R. P. Feynman, "Slow Electrons in a Polar Crystal," Phys. Rev. **97**, 660 (1955). DOI: [10.1103/PhysRev.97.660](https://doi.org/10.1103/PhysRev.97.660)
