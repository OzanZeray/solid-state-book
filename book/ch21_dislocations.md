# Chapter 21: Dislocations

## Theoretical vs Experimental Shear Strength

The theoretical shear strength of a perfect crystal is tau_th ~ G / (2*pi), where G is the shear modulus. Real crystals yield at stresses 100-10,000 times lower due to dislocation motion.

| Crystal    | G (GPa) | tau_th = G/2pi (GPa) | tau_exp (MPa) | tau_th / tau_exp |
|-----------|---------|---------------------|--------------|-----------------|
| Fe (alpha) | 81      | 12.9                | 27.5         | 470             |
| Cu         | 48      | 7.6                 | 0.98         | 7800            |
| Al         | 26      | 4.1                 | 0.78         | 5300            |
| NaCl       | 13      | 2.1                 | 0.75         | 2800            |
| Zn         | 43      | 6.8                 | 0.18         | 38000           |

This enormous discrepancy, first recognized by Frenkel (1926), motivated the independent proposals of dislocations by Taylor, Orowan, and Polanyi in 1934.

## TEM Observation of Dislocations

Transmission electron microscopy provides direct imaging of dislocation lines through diffraction contrast. Taylor and Christian (1967) studied dislocation structures in deformed metals using TEM.

> "Electron microscopy reveals that the dislocation density in lightly deformed copper is approximately 10^8 cm^-2, increasing to 10^12 cm^-2 after heavy cold working." -- Taylor & Christian, Phil. Mag. 15, 893 (1967)

| Material (condition)         | Dislocation density rho (cm^-2) | Method |
|-----------------------------|-------------------------------|--------|
| Annealed Cu single crystal   | 10^6 - 10^7                   | TEM    |
| Lightly deformed Cu          | 10^8 - 10^9                   | TEM    |
| Heavily cold-worked Cu       | 10^11 - 10^12                 | TEM    |
| Si (dislocation-free wafer)  | < 10^0                        | X-ray  |
| GaAs (LEC grown)             | 10^3 - 10^5                   | Etch pit |
| Stainless steel (annealed)   | 10^7 - 10^8                   | TEM    |
| Stainless steel (work-hardened)| 10^10 - 10^11               | TEM    |

## Whisker Strength: Approaching Theoretical Limits

Metal whiskers are nearly defect-free single crystals that approach the theoretical shear strength. Brenner (1956) performed systematic tensile tests on metal whiskers.

| Material | Whisker diameter (micro-m) | Tensile strength (GPa) | G/tau ratio | Theoretical max (GPa) |
|----------|--------------------------|----------------------|-------------|----------------------|
| Fe       | 1.6                      | 13.2                 | 6.1         | 12.9                 |
| Cu       | 1.25                     | 2.9                  | 16.5        | 7.6                  |
| Ag       | 4                        | 1.7                  | 17.6        | 4.8                  |
| Sn       | 15                       | 0.75                 | 25          | 2.9                  |
| Si (nanowire) | 0.1               | 12                   | 5.6         | 11.2                 |

Iron whiskers achieve strengths remarkably close to the theoretical limit, confirming that bulk weakness originates from dislocations rather than from intrinsic atomic bonding.

## Burgers Vectors and Slip Systems

| Crystal structure | Slip plane | Slip direction | Burgers vector b      | Number of slip systems |
|------------------|------------|----------------|----------------------|----------------------|
| FCC              | {111}      | <110>          | a/2 <110>            | 12                   |
| BCC              | {110}      | <111>          | a/2 <111>            | 12 (primary)         |
| BCC              | {112},{123}| <111>          | a/2 <111>            | 24, 24               |
| HCP              | (0001)     | <11-20>        | a/3 <11-20>          | 3 (basal)            |
| Diamond cubic    | {111}      | <110>          | a/2 <110>            | 12                   |
| NaCl             | {110}      | <1-10>         | a/2 <1-10>           | 6                    |

## Work Hardening: Stress-Strain Data

The Taylor hardening model predicts the flow stress: tau = alpha * G * b * sqrt(rho), where alpha ~ 0.2-0.5.

| Material | Stage     | Hardening rate d(tau)/d(gamma) | rho (cm^-2)  | tau (MPa) |
|----------|-----------|-------------------------------|-------------|-----------|
| Cu       | Stage I   | G/40000                       | 10^7        | 0.5       |
| Cu       | Stage II  | G/300                         | 10^9        | 15        |
| Cu       | Stage III | decreasing                    | 10^10       | 50        |
| Al       | Stage II  | G/200                         | 10^9        | 8         |

Stage I (easy glide) involves single-slip with low hardening. Stage II (linear hardening) corresponds to multi-slip with rapid dislocation multiplication. Stage III (parabolic) reflects dynamic recovery via cross-slip.

## Peierls-Nabarro Stress

The lattice friction stress (Peierls stress) controls the intrinsic resistance to dislocation motion:

| Material | Peierls stress tau_P (MPa) | tau_P / G     | Character  |
|----------|---------------------------|---------------|------------|
| Al       | 0.2                       | 8 x 10^-6    | Very mobile |
| Cu       | 0.5                       | 1 x 10^-5    | Very mobile |
| Fe (screw)| 370                      | 4.6 x 10^-3  | High friction|
| W (screw) | 900                      | 5.5 x 10^-3  | High friction|
| Si (300 K)| ~2000                    | 3 x 10^-2    | Covalent    |
| Diamond   | >10^4                    | >10^-2        | Covalent    |

BCC metals and covalent crystals show high Peierls stresses for screw dislocations due to their compact, non-planar core structures.

## References

1. A. Taylor and B. J. Christian, "Dislocation Arrangements in Deformed Copper," Phil. Mag. **15**, 893 (1967). DOI: [10.1080/14786436708221636](https://doi.org/10.1080/14786436708221636)
2. S. S. Brenner, "Tensile Strength of Whiskers," J. Appl. Phys. **27**, 1484 (1956). DOI: [10.1063/1.1722294](https://doi.org/10.1063/1.1722294)
3. J. Frenkel, "Zur Theorie der Elastizitatsgrenze und der Festigkeit kristallinischer Korper," Z. Phys. **37**, 572 (1926). DOI: [10.1007/BF01397292](https://doi.org/10.1007/BF01397292)
4. G. I. Taylor, "The Mechanism of Plastic Deformation of Crystals," Proc. Roy. Soc. A **145**, 362 (1934). DOI: [10.1098/rspa.1934.0106](https://doi.org/10.1098/rspa.1934.0106)
5. J. P. Hirth and J. Lothe, *Theory of Dislocations*, 2nd ed. (Wiley, 1982).
