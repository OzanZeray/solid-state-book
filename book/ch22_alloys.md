# Chapter 22: Alloys

## The Kondo Effect: Resistance Minimum in Dilute Magnetic Alloys

Kondo (1964) explained the anomalous resistance minimum observed in dilute alloys of magnetic impurities in nonmagnetic hosts. The third-order perturbation theory yields a ln(T) contribution to resistivity that competes with the phonon T^5 term, producing a minimum.

> "It is shown that the s-d interaction gives rise to a term proportional to log T in the resistivity of dilute magnetic alloys." -- J. Kondo, Prog. Theor. Phys. 32, 37 (1964)

The Kondo temperature T_K marks the crossover from weak-coupling (perturbative) to strong-coupling (screened) regimes.

| Host-Impurity system | T_K (K)    | Impurity spin S | Resistance minimum T_min (K) |
|---------------------|-----------|----------------|------------------------------|
| Cu:Fe                | 22        | 5/2            | ~10                          |
| Cu:Mn                | 0.01      | 5/2            | ~1                           |
| Cu:Cr                | 1-2       | 3/2            | ~5                           |
| Au:Fe                | 0.3       | 5/2            | ~3                           |
| Au:V                 | 300       | 1              | > 300                        |
| La:Ce (heavy fermion)| ~5        | 5/2            | ~5                           |

Systems with high T_K (Au:V) show the resistance minimum at high temperature; low T_K systems (Cu:Mn) exhibit the minimum near 1 K.

## Nordheim Rule and Residual Resistivity

The Nordheim rule states that the residual resistivity of a substitutional binary alloy A_{1-x}B_x is proportional to x(1-x):

Delta_rho = C * x(1-x)

| Alloy system  | C (micro-Ohm*cm) | x at maximum | rho_max (micro-Ohm*cm) |
|--------------|-------------------|-------------|------------------------|
| Cu-Au         | 5.7               | 0.50        | 1.43                   |
| Cu-Zn         | 0.30              | 0.50        | 0.075                  |
| Cu-Ni         | 1.14              | 0.50        | 0.285                  |
| Ag-Au         | 3.6               | 0.50        | 0.90                   |
| Cu-Ge         | 4.0               | 0.50        | 1.00                   |

The parabolic concentration dependence arises from the Born approximation for scattering from random substitutional disorder.

## Order-Disorder Transition in Cu3Au

Cu3Au undergoes a first-order order-disorder transition at T_c = 663 K. Below T_c, Au atoms occupy corner sites and Cu atoms occupy face-center sites of the cubic unit cell (L1_2 structure).

| Property                        | Ordered (T < 663 K) | Disordered (T > 663 K) |
|--------------------------------|---------------------|------------------------|
| Structure                       | L1_2 (Pm-3m)       | FCC (Fm-3m)            |
| Lattice parameter               | 3.749 A             | 3.753 A                |
| Long-range order parameter S    | 1.0 (at 0 K)       | 0                      |
| Electrical resistivity          | ~3.7 micro-Ohm*cm   | ~15.5 micro-Ohm*cm    |
| Superlattice reflections (100)  | Present             | Absent                 |

The resistivity drops by a factor of ~4 upon ordering, because the periodic potential of the ordered alloy drastically reduces electron scattering.

## Pb-Sn Eutectic Phase Diagram

The Pb-Sn system is the classic eutectic, long used as solder (now largely replaced by Pb-free alternatives for environmental reasons).

| Feature              | Composition (wt% Sn) | Temperature (C) |
|---------------------|----------------------|-----------------|
| Melting point of Pb  | 0                    | 327.5           |
| Melting point of Sn  | 100                  | 231.9           |
| Eutectic point       | 61.9                 | 183             |
| Max solid sol. Sn in Pb (alpha) | 19.2     | 183             |
| Max solid sol. Pb in Sn (beta)  | 2.6      | 183             |

The eutectic microstructure consists of alternating lamellae of alpha (Pb-rich) and beta (Sn-rich) phases with a characteristic spacing of ~1-5 micro-m depending on cooling rate.

## Hume-Rothery Rules: Solid Solution Formation

Hume-Rothery identified empirical conditions for extensive solid solubility:

| Rule                  | Criterion                  | Example (favorable) | Example (unfavorable) |
|----------------------|---------------------------|--------------------|-----------------------|
| Atomic size          | < 15% difference           | Cu-Ni (2.6%)      | Cu-Pb (37%)           |
| Electronegativity    | Similar values             | Cu-Ni              | Cu-O                  |
| Valence              | Same valence preferred     | Cu-Ni (both +1/+2)| Cu-Si                 |
| Crystal structure    | Same structure             | Cu-Ni (both FCC)  | Cu-Fe (FCC vs BCC)    |

Cu-Ni satisfies all four rules and forms a complete solid solution at all compositions.

## Electron Compounds (Hume-Rothery Phases)

Certain intermetallic phases occur at specific electron-to-atom (e/a) ratios:

| Phase type | e/a ratio | Structure                  | Examples              |
|-----------|-----------|---------------------------|-----------------------|
| alpha      | < 1.4     | FCC solid solution         | Cu-Zn (< 35% Zn)     |
| beta       | 3/2       | BCC (CsCl type)            | CuZn, Cu3Al, AgCd     |
| gamma      | 21/13     | Complex cubic (52 atoms)   | Cu5Zn8, Cu9Al4        |
| epsilon    | 7/4       | HCP                        | CuZn3, AgCd3          |

## Heavy Fermion Behavior

In some rare-earth and actinide alloys, the Kondo effect involves the entire lattice of magnetic ions, producing a coherent heavy-fermion state with effective masses m* ~ 100-1000 m_e.

| Compound  | gamma (mJ/mol*K^2) | m*/m_e  | T_K (K) | Ground state          |
|----------|--------------------|----|---------|------------------------|
| CeAl3     | 1620               | ~800    | 5       | Heavy Fermi liquid     |
| CeCu6     | 1600               | ~700    | 5       | Heavy Fermi liquid     |
| UPt3      | 450                | ~200    | 20      | Unconventional SC      |
| UBe13     | 1100               | ~500    | 8       | Unconventional SC      |
| CeCoIn5   | 290                | ~130    | 50      | d-wave SC              |

The enormous electronic specific heat coefficient gamma reflects the large density of states at the Fermi level from the renormalized f-electron bands.

## References

1. J. Kondo, "Resistance Minimum in Dilute Magnetic Alloys," Prog. Theor. Phys. **32**, 37 (1964). DOI: [10.1143/PTP.32.37](https://doi.org/10.1143/PTP.32.37)
2. L. Nordheim, "Zur Elektronentheorie der Metalle. II," Ann. Phys. **401**, 641 (1931). DOI: [10.1002/andp.19314010503](https://doi.org/10.1002/andp.19314010503)
3. C. S. Barrett, "A Low Temperature Transformation in Lithium," Phys. Rev. **72**, 245 (1947). (Cu3Au data by Cowley, 1950)
4. W. Hume-Rothery et al., "The Freezing Points, Melting Points, and Solid Solubility Limits of the Alloys of Silver and Copper with the Elements of the B Sub-Groups," Phil. Trans. R. Soc. A **233**, 1 (1934). DOI: [10.1098/rsta.1934.0014](https://doi.org/10.1098/rsta.1934.0014)
5. G. R. Stewart, "Heavy-fermion systems," Rev. Mod. Phys. **56**, 755 (1984). DOI: [10.1103/RevModPhys.56.755](https://doi.org/10.1103/RevModPhys.56.755)
