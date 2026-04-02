# Chapter 16: Dielectrics and Ferroelectrics

## Dielectric Constants of Insulators

The dielectric constant epsilon_r describes the polarization response of a material to an applied electric field. Static values at room temperature:

| Material       | epsilon_r (static) | epsilon_r (optical) | Dominant mechanism  |
|---------------|-------------------|--------------------|--------------------|
| Vacuum         | 1.000             | 1.000              | --                 |
| Diamond        | 5.7               | 5.7                | Electronic         |
| NaCl           | 5.9               | 2.34               | Ionic + electronic |
| SiO2 (quartz)  | 3.78              | 2.13               | Ionic + electronic |
| H2O (liquid)   | 80.4              | 1.78               | Orientational      |
| BaTiO3 (25 C)  | ~1700             | 5.4                | Ferroelectric      |
| SrTiO3 (4 K)   | ~24000            | 5.2                | Quantum paraelectric |

## Ferroelectric Phase Transition in BaTiO3

Barium titanate is the prototypical displacive ferroelectric. Samara (1971) measured the temperature dependence of the dielectric constant through the cubic-to-tetragonal transition at T_C = 120 C.

> "At the Curie point, the dielectric constant shows a sharp peak exceeding 10,000, consistent with a first-order transition." -- Samara, Ferroelectrics 2, 277 (1971)

| Temperature (C) | epsilon_r (heating) | Phase       |
|-----------------|--------------------|----|
| 25              | 1700               | Tetragonal  |
| 80              | 3200               | Tetragonal  |
| 100             | 5500               | Tetragonal  |
| 115             | 9000               | Tetragonal  |
| 120 (T_C)       | >10000             | Transition  |
| 130             | 6200               | Cubic       |
| 150             | 3500               | Cubic       |
| 200             | 2000               | Cubic       |

Above T_C, the Curie-Weiss law applies: epsilon_r = C / (T - T_0) with C ~ 1.5 x 10^5 K and T_0 ~ 383 K.

## BaTiO3 Structural Phase Sequence

| Phase        | Temperature range | Crystal system | Spontaneous polarization (micro-C/cm^2) |
|-------------|-------------------|----------------|---------------------------------------|
| Rhombohedral | < -90 C           | Rhombohedral   | ~10 along [111]                       |
| Orthorhombic | -90 to 5 C        | Orthorhombic   | ~14 along [011]                       |
| Tetragonal   | 5 to 120 C        | Tetragonal     | 26 along [001]                        |
| Cubic        | > 120 C            | Cubic (Pm3m)   | 0                                     |

## Polarization-Electric Field Hysteresis

The P-E hysteresis loop is the defining signature of ferroelectricity. For BaTiO3 single crystal at room temperature:

- Saturation polarization P_s: 26 micro-C/cm^2
- Remanent polarization P_r: 22 micro-C/cm^2
- Coercive field E_c: ~1 kV/cm

For comparison, PZT (PbZr_0.52Ti_0.48O_3) ceramics show P_r ~ 35 micro-C/cm^2 and E_c ~ 10-15 kV/cm.

## Piezoelectric Coefficients

Piezoelectric materials convert between mechanical stress and electric polarization. The d_33 coefficient (longitudinal) is a key figure of merit.

| Material               | d_33 (pC/N) | T_C (C) | Application               |
|-----------------------|-------------|---------|--------------------------|
| Quartz (alpha-SiO2)    | 2.3         | 573     | Frequency standards       |
| BaTiO3 (ceramic)       | 190         | 120     | Capacitors                |
| PZT-5A                 | 374         | 365     | Actuators, transducers    |
| PZT-5H                 | 593         | 193     | Sensors                   |
| PMN-PT single crystal  | 1500-2800   | 130-170 | Medical ultrasound        |
| PVDF polymer           | -33         | --      | Flexible sensors          |
| LiNbO3                 | 6           | 1210    | SAW devices, optics       |
| AlN                    | 5.5         | --      | MEMS, thin film BAW       |

## Soft Mode Theory

The ferroelectric transition is driven by the softening of a transverse optical phonon. As T approaches T_C from above, the soft mode frequency decreases: omega_TO^2 ~ (T - T_C).

Cowley (1962) and Shirane et al. (1970) confirmed soft mode behavior in SrTiO3 and BaTiO3 via neutron scattering. In SrTiO3, the soft mode frequency drops to ~10 cm^-1 at 4 K but never reaches zero -- SrTiO3 is a quantum paraelectric where zero-point fluctuations suppress long-range order.

| Material | Soft mode frequency at T_C + 50 K (cm^-1) | Transition type |
|----------|-------------------------------------------|-----------------|
| BaTiO3   | ~50                                        | First order     |
| PbTiO3   | ~80                                        | First order     |
| SrTiO3   | ~12 (at 4 K)                               | Suppressed      |
| KNbO3    | ~55                                        | First order     |

## References

1. G. A. Samara, "The Effect of Pressure on the Dielectric Properties of BaTiO3," Ferroelectrics **2**, 277 (1971). DOI: [10.1080/00150197108234102](https://doi.org/10.1080/00150197108234102)
2. G. Shirane et al., "Soft Ferroelectric Modes in Lead Titanate," Phys. Rev. B **2**, 155 (1970). DOI: [10.1103/PhysRevB.2.155](https://doi.org/10.1103/PhysRevB.2.155)
3. R. A. Cowley, "Temperature Dependence of a Transverse Optic Mode in Strontium Titanate," Phys. Rev. Lett. **9**, 159 (1962). DOI: [10.1103/PhysRevLett.9.159](https://doi.org/10.1103/PhysRevLett.9.159)
4. S.-E. Park and T. R. Shrout, "Ultrahigh strain and piezoelectric behavior in relaxor based ferroelectric single crystals," J. Appl. Phys. **82**, 1804 (1997). DOI: [10.1063/1.365983](https://doi.org/10.1063/1.365983)
5. M. E. Lines and A. M. Glass, *Principles and Applications of Ferroelectrics and Related Materials* (Oxford, 1977).
