# Chapter 6: Free Electron Fermi Gas

The free electron model treats valence electrons in a metal as non-interacting fermions confined to the crystal volume. Despite its simplicity, it explains the electronic heat capacity, electrical and thermal conductivity, and the Hall effect with remarkable accuracy.

---

## 6.1 Energy Levels and the Fermi–Dirac Distribution

At $T = 0$, all states up to the Fermi energy $E_F$ are occupied:

$$E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$$

| Metal | $n$ (10²⁸ m⁻³) | $E_F$ (eV) | $T_F$ (10⁴ K) | $v_F$ (10⁶ m/s) | $k_F$ (Å⁻¹) |
|-------|---------------|-----------|--------------|----------------|------------|
| Li | 4.70 | 4.74 | 5.51 | 1.29 | 1.12 |
| Na | 2.65 | 3.24 | 3.77 | 1.07 | 0.92 |
| K | 1.40 | 2.12 | 2.46 | 0.86 | 0.75 |
| Cu | 8.47 | 7.04 | 8.16 | 1.57 | 1.36 |
| Ag | 5.86 | 5.49 | 6.38 | 1.39 | 1.20 |
| Au | 5.90 | 5.53 | 6.42 | 1.40 | 1.21 |

Fermi temperatures are ~10⁴ K — far above room temperature. Only electrons near $E_F$ participate in thermal and transport processes.

---

## 6.2 Heat Capacity of the Electron Gas

The electronic heat capacity: $C_{el} = \gamma T$, where $\gamma$ is the **Sommerfeld coefficient**.

### Martin's Precision Measurements (1968)

Douglas L. Martin at the National Research Council of Canada measured the specific heat of pure Cu, Ag, and Au below 3 K with extraordinary precision [Martin 1968].

From the original paper: *"The electronic specific-heat coefficient γ and the limiting low-temperature Debye temperature (Θ₀) are estimated as 165.2±0.8 μcal/°K² (g atom) and 345.8±1.2°K for copper, 153.1±0.9 μcal/°K² (g atom) and 227.3±0.6°K for silver, and 165.1±1.0 μcal/°K² (g atom) and 162.3±0.5°K for gold."* [Martin 1968, p. 650]

The data were fitted to: $C = \gamma T + [464.34/(\Theta_D^0)^3]T^3$ (Table II, p. 652).

**Sample purity** (Table I, p. 651): Cu sample 140.663 g with Fe < 0.2 ppm, Ag 134.271 g with Fe = 0.43 ppm, Au 198.887 g with Fe = 0.16 ppm — all vacuum-cast to avoid oxide contamination.

| Metal | $\gamma_{exp}$ (mJ/mol·K²) | $\gamma_{free}$ (mJ/mol·K²) | $m^*/m_e$ | $\Theta_D$ (K) |
|-------|--------------------------|---------------------------|----------|--------------|
| Li | 1.63 | 0.749 | 2.18 | — |
| Na | 1.38 | 1.094 | 1.26 | — |
| K | 2.08 | 1.668 | 1.25 | — |
| Cu | **0.695** | 0.505 | **1.38** | **345.8** |
| Ag | **0.646** | 0.645 | **1.01** | **227.3** |
| Au | **0.729** | 0.642 | **1.14** | **162.3** |
| Al | 1.35 | 0.912 | 1.48 | — |

*Bold values: directly from Martin (1968), Table II. $m^*/m_e = \gamma_{exp}/\gamma_{free}$.*

Silver is nearly free-electron-like ($m^*/m_e = 1.01$). Martin noted that *"the γ value for gold is significantly lower than previously reported values"* — his improved calorimetry resolved discrepancies from earlier work.

### Heavy Fermions

In certain rare-earth compounds, $\gamma$ is enormous:

| Compound | $\gamma$ (mJ/mol·K²) | Notes |
|----------|---------------------|-------|
| CeAl₃ | 1620 | prototypical heavy fermion |
| CeCu₂Si₂ | 1000 | first heavy fermion superconductor |
| UBe₁₃ | 1100 | |
| Cu (comparison) | 0.695 | normal metal |

The effective mass in CeAl₃ is $m^* \approx 1000 \, m_e$.

---

## 6.3 Electrical Resistivity

### The Matula Reference Data (1979)

Matula compiled the definitive recommended resistivity values for Cu, Au, Pd, and Ag from cryogenic to beyond the melting point — a 904-citation NIST reference paper [Matula 1979].

| $T$ (K) | $\rho$ (μΩ·cm) |
|---------|----------------|
| 4 | 0.002 |
| 10 | 0.002 |
| 20 | 0.008 |
| 40 | 0.054 |
| 60 | 0.162 |
| 80 | 0.322 |
| 100 | 0.520 |
| 150 | 0.963 |
| 200 | 1.358 |
| 250 | 1.524 |
| 300 | **1.678** |
| 400 | 2.402 |
| 500 | 3.090 |
| 600 | 3.792 |
| 800 | 5.262 |
| 1000 | 6.858 |

*From Matula (1979), J. Phys. Chem. Ref. Data 8, 1147.*

Residual resistivity ratio RRR = $\rho(300K)/\rho(4K) \approx 840$. Below ~40 K: Bloch-Grüneisen $T^5$ behavior; above ~150 K: nearly linear in $T$.

---

## 6.4 Hall Effect

The Hall coefficient: $R_H = E_y/(j_x B_z) = -1/(ne)$ for free electrons.

| Metal | $R_H$ (exp) (10⁻¹¹ m³/C) | $-1/ne$ (free) | Sign |
|-------|--------------------------|----------------|------|
| Li | −1.7 | −1.3 | − (electron) |
| Na | −2.5 | −2.4 | − |
| K | −4.2 | −4.5 | − |
| Cu | −0.55 | −0.74 | − |
| Ag | −0.84 | −1.1 | − |
| Au | −0.72 | −1.1 | − |
| Al | −0.30 | −0.35 | − |
| **Be** | **+2.4** | — | **+ (hole!)** |
| **Zn** | **+0.33** | — | **+** |
| **Cd** | **+0.60** | — | **+** |

*From Hurd (2012), The Hall Effect in Metals and Alloys (1350 citations).*

Be, Zn, and Cd have **positive** Hall coefficients — indicating hole-like carriers. This anomaly requires band theory (Ch. 7).

---

## 6.5 Wiedemann–Franz Law

$$\frac{\kappa}{\sigma T} = L_0 = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 = 2.44 \times 10^{-8} \text{ W·Ω/K²}$$

| Metal | $L$ (10⁻⁸ W·Ω/K²) |
|-------|-------------------|
| Cu | 2.23 |
| Ag | 2.31 |
| Au | 2.35 |
| Al | 2.14 |
| Fe | 2.61 |
| W | 3.04 |
| Pb | 2.47 |

*At 273 K. Theoretical: $L_0 = 2.44$.*

Agreement within ~10%. Völklein et al. (2009) showed the Wiedemann-Franz law holds even for individual metallic nanowires [Völklein 2009].

---

## References

1. **Martin, D. L.** (1968). "Specific Heats below 3°K of Pure Copper, Silver, and Gold, and of Extremely Dilute Gold–Transition-Metal Alloys." *Phys. Rev.* **170**, 650–655. DOI: [10.1103/PhysRev.170.650](https://doi.org/10.1103/PhysRev.170.650). — *γ and Θ_D for Cu, Ag, Au with sub-ppm purity. Table I: sample weights and impurities. Table II: fitted coefficients with 95% confidence limits.*

2. **Matula, R. A.** (1979). "Electrical Resistivity of Copper, Gold, Palladium, and Silver." *J. Phys. Chem. Ref. Data* **8**, 1147–1298. DOI: [10.1063/1.555614](https://doi.org/10.1063/1.555614). — *Recommended Cu resistivity from cryogenic to liquid. 904 citations.*

3. **Hurd, C.** (2012). *The Hall Effect in Metals and Alloys.* Springer. — *Comprehensive Hall coefficient compilation. 1350 citations.*

4. **Völklein, F.** et al. (2009). "The experimental investigation of thermal conductivity and the Wiedemann-Franz law for single metallic nanowires." *Nanotechnology* **20**, 325706. DOI: [10.1088/0957-4484/20/32/325706](https://doi.org/10.1088/0957-4484/20/32/325706).
