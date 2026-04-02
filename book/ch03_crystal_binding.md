# Chapter 3: Crystal Binding and Elastic Constants

Why do atoms form crystals? The answer lies in the lowering of total energy when atoms come together in an ordered arrangement. The nature of the binding force determines the crystal structure, the cohesive energy, and the elastic properties.

---

## 3.1 Crystals of Inert Gases

The noble gas solids (Ne, Ar, Kr, Xe) are the simplest crystals: bound entirely by the weak van der Waals interaction, all crystallizing in the fcc structure.

### Van der Waals–London Interaction and the Lennard-Jones Potential

The total interaction is described by the **Lennard-Jones potential**:

$$U(r) = 4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^{6}\right]$$

Boato and Casanova (1961) determined self-consistent LJ parameters for all noble gases from second virial coefficients, viscosity, and crystal properties. Anderson and Swenson (1975) measured the equations of state of solid Ar, Kr, and Xe under pressure, providing definitive cohesive energy and bulk modulus data [Anderson & Swenson 1975].

| | $\varepsilon/k_B$ (K) | $\sigma$ (Å) | $a$ (Å) | $R_{nn}$ (Å) | $E_{coh}$ (meV) | $B$ (GPa) |
|---|---|---|---|---|---|---|
| Ne | 35.7 | 2.789 | 4.464 | 3.156 | 20 | 1.1 |
| Ar | 119.8 | 3.405 | 5.311 | 3.755 | 80 | 2.7 |
| Kr | 164.0 | 3.624 | 5.646 | 3.992 | 116 | 3.5 |
| Xe | 230.0 | 3.963 | 6.129 | 4.334 | 170 | 3.6 |

*$R_{nn} = a/\sqrt{2}$. LJ parameters from Boato & Casanova (1961); cohesive energies from Anderson & Swenson (1975).*

---

## 3.2 Ionic Crystals

### Madelung Energy

The dominant cohesive contribution in ionic crystals is the electrostatic (Madelung) energy:

$$U_{Madelung} = -\frac{N\alpha q^2}{4\pi\varepsilon_0 R}$$

where $\alpha$ is the **Madelung constant**. Mestechkin (2000) tabulated over 200 Madelung constants [Mestechkin 2000].

| Structure | Madelung constant $\alpha$ | Example |
|-----------|--------------------------|---------|
| NaCl (B1) | 1.7476 | NaCl, MgO, LiF |
| CsCl (B2) | 1.7627 | CsCl, CsBr |
| Zinc blende (B3) | 1.6381 | ZnS, GaAs |
| Wurtzite (B4) | 1.6413 | ZnO, AlN |
| Fluorite | 2.5194 | CaF₂, UO₂ |
| Rutile | 2.408 | TiO₂ |

### Born–Mayer Lattice Energies

The Born-Haber cycle (purely experimental thermodynamic data) agrees with the Born–Mayer electrostatic model to within ~1%:

| Crystal | Expt. (kJ/mol) | Calc. (kJ/mol) | Diff. (%) |
|---------|----------------|----------------|-----------|
| LiF | 1037 | 1030 | 0.7 |
| NaCl | 786 | 778 | 1.0 |
| KCl | 715 | 709 | 0.8 |
| KBr | 682 | 674 | 1.2 |
| RbCl | 689 | 681 | 1.2 |
| CsCl | 657 | 649 | 1.2 |

---

## 3.3 Cohesive Energies Compared

| Crystal | $E_{coh}$ (eV/atom) | Bonding type |
|---------|-------------------|-------------|
| C (diamond) | 7.37 | covalent |
| Si | 4.63 | covalent |
| Ge | 3.85 | covalent |
| SiC | 6.34 | covalent |
| Na | 1.11 | metallic |
| Cu | 3.49 | metallic |
| Fe | 4.28 | metallic |
| W | 8.90 | metallic |
| NaCl | 3.28 | ionic (per ion pair) |

---

## 3.4 Elastic Constants

### Ultrasonic Measurement Method

The standard technique measures the velocity of ultrasonic waves along crystallographic directions. The key relations for cubic crystals:

- **[001] longitudinal**: $\rho v^2 = c_{11}$
- **[001] transverse**: $\rho v^2 = c_{44}$
- **[011] longitudinal**: $\rho v^2 = (c_{11} + c_{12} + 2c_{44})/2$
- **[011] transverse** (polarized [01̄1]): $\rho v^2 = (c_{11} - c_{12})/2$

### The Overton–Gaffney Experiment (1955)

Overton and Gaffney performed the definitive measurement of copper's elastic constants from 4.2 K to 300 K using the ultrasonic pulse-echo technique at 10 MHz [Overton & Gaffney 1955]. Their paper (636 citations) remains the standard reference for Cu elastic data.

From the original paper: *"The ultrasonic pulse technique has been used in conjunction with a specially devised cryogenic technique to measure the velocities of 10-Mc/sec acoustic waves in copper single crystals in the range from 4.2°K to 300°K."* [Overton & Gaffney 1955, p. 969]

**Experimental details:**
- (001) copper crystal: length 5.3622 cm at 27.4°C
- (011) copper crystal: length 5.7833 cm at 20°C
- Ultrasonic frequency: 10 MHz
- Precision: $c_{44}$ to ±0.25%, velocities to ±0.08%

### Elastic Constants of Cubic Crystals

| Crystal | $c_{11}$ | $c_{12}$ | $c_{44}$ | $A = 2c_{44}/(c_{11}-c_{12})$ |
|---------|---------|---------|---------|------|
| Cu | 16.84 | 12.14 | 7.54 | 3.21 |
| Al | 10.82 | 6.13 | 2.85 | 1.21 |
| Au | 18.60 | 15.70 | 4.20 | 2.90 |
| Fe | 23.10 | 13.50 | 11.60 | 2.42 |
| W | 52.33 | 20.45 | 16.07 | 1.01 |
| NaCl | 4.87 | 1.24 | 1.26 | 0.69 |
| KCl | 4.07 | 0.71 | 0.63 | 0.37 |
| LiF | 11.12 | 4.20 | 6.28 | 1.82 |
| MgO | 29.71 | 9.54 | 15.57 | 1.54 |
| Si | 16.58 | 6.39 | 7.96 | 1.56 |
| Ge | 12.89 | 4.83 | 6.71 | 1.66 |
| Diamond | 107.6 | 12.50 | 57.74 | 1.21 |

*Units: 10¹⁰ N/m². Cu data from Overton & Gaffney (1955); alkali halides at 4.2 K from Lewis et al. (1967).*

**Anisotropy ratio** $A$: tungsten is nearly isotropic ($A = 1.01$), copper is strongly anisotropic ($A = 3.21$). Overton and Gaffney noted: *"The isotropy, $(c_{11}-c_{12})/2c_{44}$, was observed to remain practically constant from 4.2°K to 180°K."* [Overton & Gaffney 1955, p. 969]

### Bulk Modulus

$$B = \frac{c_{11} + 2c_{12}}{3}$$

| Material | $B$ (GPa) | Notes |
|----------|----------|-------|
| Diamond | 443 | hardest known |
| W | 310 | highest among metals |
| Fe | 167 | |
| Cu | 137 | |
| Si | 98 | |
| Al | 76 | |
| NaCl | 24 | |
| KCl | 18 | |
| Na | 6.3 | softest cubic metal |
| Xe (solid) | 3.6 | van der Waals |

Slater (1924) performed the first compressibility measurements on alkali halides [Slater 1924], establishing the experimental basis that softer crystals have larger ions.

---

## References

1. **Anderson, M. S. and Swenson, C. A.** (1975). "Experimental equations of state for the rare gas solids." *J. Phys. Chem. Solids* **36**, 145. DOI: [10.1016/0022-3697(75)90004-9](https://doi.org/10.1016/0022-3697(75)90004-9).

2. **Overton, W. C. Jr. and Gaffney, J.** (1955). "Temperature Variation of the Elastic Constants of Cubic Elements. I. Copper." *Phys. Rev.* **98**, 969–977. DOI: [10.1103/PhysRev.98.969](https://doi.org/10.1103/PhysRev.98.969). — *Definitive Cu elastic constants from 4.2 K to 300 K. 636 citations.*

3. **Lewis, J. T., Lehoczky, A., and Briscoe, C. V.** (1967). "Elastic Constants of the Alkali Halides at 4.2 K." *Phys. Rev.* **161**, 877. DOI: [10.1103/PhysRev.161.877](https://doi.org/10.1103/PhysRev.161.877). — *Complete elastic constants of all alkali halides. 331 citations.*

4. **Slater, J. C.** (1924). "Compressibility of the Alkali Halides." *Phys. Rev.* **23**, 488. DOI: [10.1103/PhysRev.23.488](https://doi.org/10.1103/PhysRev.23.488). — *First compressibility measurements.*

5. **Schwerdtfeger, P., Gaston, N., and Krawczyk, R. P.** (2006). "Extension of the Lennard-Jones potential..." *Phys. Rev. B* **73**, 064112. DOI: [10.1103/PhysRevB.73.064112](https://doi.org/10.1103/PhysRevB.73.064112).

6. **Mestechkin, M. M.** (2000). "Electrostatic parameters of ionic crystals." *J. Phys. Chem. Ref. Data* **29**, 571.
