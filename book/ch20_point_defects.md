# Chapter 20: Point Defects

## Vacancy Formation Energy

The equilibrium vacancy concentration follows n_v / N = exp(-E_f / kT), where E_f is the formation energy. Simmons and Balluffi (1960) determined E_f in aluminum by simultaneously measuring thermal expansion (all sites, including vacant) and lattice parameter (occupied sites only).

> "The equilibrium concentration of vacancies in aluminum near the melting point is approximately 9.4 x 10^-4, corresponding to a formation energy of 0.76 eV." -- Simmons & Balluffi, Phys. Rev. 117, 52 (1960)

| Metal | E_f (eV) | E_m (migration, eV) | E_a = E_f + E_m (eV) | Method                  |
|-------|---------|---------------------|----------------------|-------------------------|
| Al    | 0.76    | 0.65                | 1.41                 | Differential dilatometry |
| Cu    | 1.28    | 0.70                | 1.98                 | Quenching + resistivity  |
| Au    | 0.94    | 0.83                | 1.77                 | Quenching + resistivity  |
| Ag    | 1.09    | 0.66                | 1.75                 | Positron annihilation    |
| Pt    | 1.35    | 1.43                | 2.78                 | Quenching experiments    |
| W     | 3.60    | 1.70                | 5.30                 | Resistivity recovery     |
| Fe    | 1.60    | 0.55                | 2.15                 | Resistivity recovery     |
| Ni    | 1.79    | 1.04                | 2.83                 | Positron annihilation    |

High-melting-point metals (W, Pt) have correspondingly large formation energies. The vacancy concentration in Al at the melting point (933 K) is ~10^-4, meaning roughly 1 in 10,000 sites is vacant.

## F-Center Absorption in Alkali Halides

F-centers (Farbe = color) are electrons trapped at anion vacancies. They produce broad optical absorption bands that give alkali halide crystals their characteristic colors. Seitz (1946) provided the first comprehensive review.

> "The color centers in alkali halides provide a beautiful example of the quantum mechanics of a particle in a potential well." -- Seitz, Rev. Mod. Phys. 18, 384 (1946)

| Crystal | F-center absorption peak (nm) | F-center peak (eV) | Lattice constant a (A) | Color of crystal |
|---------|------------------------------|--------------------|-----------------------|-----------------|
| LiF     | 248                          | 5.00               | 4.03                  | Colorless (UV)  |
| LiCl    | 385                          | 3.22               | 5.13                  | Yellow          |
| NaF     | 340                          | 3.65               | 4.63                  | Pale yellow     |
| NaCl    | 465                          | 2.67               | 5.64                  | Yellow-brown    |
| NaBr    | 540                          | 2.30               | 5.97                  | Brown           |
| KCl     | 563                          | 2.20               | 6.29                  | Violet          |
| KBr     | 620                          | 2.00               | 6.60                  | Blue-green      |
| RbCl    | 620                          | 2.00               | 6.58                  | Blue-green      |

## Mollwo-Ivey Relation

The F-center absorption energy scales with the lattice constant as:

E_F = A / a^n

where A ~ 17.7 eV*A^n and n ~ 1.84. This empirical relation follows from treating the F-center as a particle in a box of size proportional to the lattice constant.

| Crystal pair | a_1 / a_2 | E_1 / E_2 (measured) | E_1 / E_2 (predicted, n=1.84) |
|-------------|-----------|---------------------|-------------------------------|
| LiF / NaCl  | 0.714     | 1.87                | 1.86                          |
| NaCl / KCl  | 0.897     | 1.21                | 1.20                          |
| KCl / KBr   | 0.953     | 1.10                | 1.09                          |
| NaBr / KBr  | 0.905     | 1.15                | 1.18                          |

The excellent agreement confirms the simple particle-in-a-box picture.

## Schottky and Frenkel Defect Equilibria

| Crystal | Dominant defect type | Formation energy (eV/pair) | Method            |
|---------|---------------------|---------------------------|-------------------|
| NaCl    | Schottky            | 2.32                       | Ionic conductivity |
| KCl     | Schottky            | 2.50                       | Ionic conductivity |
| KBr     | Schottky            | 2.53                       | Ionic conductivity |
| AgBr    | Frenkel (cation)    | 1.10                       | Ionic conductivity |
| AgCl    | Frenkel (cation)    | 1.45                       | Ionic conductivity |
| CaF2    | Frenkel (anion)     | 2.70                       | Ionic conductivity |
| UO2     | Frenkel (anion)     | 3.00                       | Neutron diffraction|

## Positron Annihilation Spectroscopy

Modern vacancy studies use positron annihilation lifetime spectroscopy (PALS). Positrons preferentially trap at vacancy sites, where the reduced electron density increases the annihilation lifetime.

| Material (state)   | Positron lifetime (ps) | Interpretation          |
|-------------------|----------------------|-------------------------|
| Al (defect-free)   | 163                  | Bulk lifetime            |
| Al (monovacancy)   | 245                  | Vacancy trapped          |
| Cu (defect-free)   | 122                  | Bulk lifetime            |
| Cu (monovacancy)   | 180                  | Vacancy trapped          |
| Fe (defect-free)   | 110                  | Bulk lifetime            |
| Fe (monovacancy)   | 175                  | Vacancy trapped          |

The lifetime increase of ~50-80% upon trapping at a vacancy provides an unambiguous defect signature.

## References

1. R. O. Simmons and R. W. Balluffi, "Measurements of Equilibrium Vacancy Concentrations in Aluminum," Phys. Rev. **117**, 52 (1960). DOI: [10.1103/PhysRev.117.52](https://doi.org/10.1103/PhysRev.117.52)
2. F. Seitz, "Color Centers in Alkali Halide Crystals," Rev. Mod. Phys. **18**, 384 (1946). DOI: [10.1103/RevModPhys.18.384](https://doi.org/10.1103/RevModPhys.18.384)
3. E. Mollwo, "Uber die Zuordnung von Verfarbungsbanden und Gitterstorungen in Alkalihalogenidkristallen," Nachr. Ges. Wiss. Gottingen **1**, 97 (1931).
4. H. F. Ivey, "Spectral Location of the Absorption Due to Color Centers in Alkali Halide Crystals," Phys. Rev. **72**, 341 (1947). DOI: [10.1103/PhysRev.72.341](https://doi.org/10.1103/PhysRev.72.341)
5. R. Krause-Rehberg and H. S. Leipner, *Positron Annihilation in Semiconductors* (Springer, 1999).
