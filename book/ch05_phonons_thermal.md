# Chapter 5: Phonons II — Thermal Properties

The thermal properties of solids — heat capacity, thermal conductivity, thermal expansion — are governed by lattice vibrations. The experimental data in this chapter demonstrate how phonon statistics and scattering processes determine these properties across an enormous temperature range.

---

## 5.1 Phonon Heat Capacity

### The Debye Model and the $T^3$ Law

At low temperatures:

$$C_V = \frac{12\pi^4}{5} N k_B \left(\frac{T}{\Theta_D}\right)^3$$

where $\Theta_D$ is the **Debye temperature**: $k_B \Theta_D = \hbar\omega_D$.

The standard test is to plot $C/T$ vs $T^2$ at low temperatures — the data should be linear:

$$\frac{C}{T} = \gamma + \beta T^2$$

where $\gamma T$ is the electronic contribution (Ch. 6) and $\beta$ gives $\Theta_D$. Parkinson (1958) performed this analysis for many metals, showing that the Debye model fits remarkably well below $\Theta_D/10$ [Parkinson 1958].

### Debye Temperatures

| Material | $\Theta_D$ (K) | Material | $\Theta_D$ (K) |
|----------|---------------|----------|---------------|
| C (diamond) | 2230 | Cu | 343 |
| Si | 645 | Au | 165 |
| Ge | 374 | Al | 428 |
| SiC | 1200 | Fe | 470 |
| MgO | 946 | W | 400 |
| NaCl | 321 | Na | 158 |
| KCl | 235 | Pb | 105 |
| LiF | 732 | Ar (solid) | 93 |

*From Abrahams et al. (1975) and Grimvall et al. (1974).*

Diamond has the highest $\Theta_D$ of any material (2230 K). At room temperature ($T/\Theta_D \approx 0.13$), diamond is far from the classical limit — this is why Einstein's 1907 quantum theory of specific heat was inspired by diamond's anomalously low heat capacity.

### Einstein Model

Einstein (1907) treated all atoms as independent oscillators at frequency $\omega_E$:

$$C_V = 3Nk_B \left(\frac{\Theta_E}{T}\right)^2 \frac{e^{\Theta_E/T}}{(e^{\Theta_E/T} - 1)^2}$$

The Einstein model correctly predicts the exponential freeze-out at $T \ll \Theta_E$ but gives $C \propto e^{-\Theta_E/T}$ instead of the correct $T^3$. The Debye model corrects this by accounting for the distribution of phonon frequencies.

---

## 5.2 Thermal Conductivity

### The Phonon Gas Model

In a nonmetallic crystal:

$$\kappa = \frac{1}{3} C_V v_s \ell$$

The temperature dependence reflects three competing scattering mechanisms:
1. **Boundary scattering** (low $T$): $\ell \approx$ crystal size, $\kappa \propto T^3$
2. **Point defect scattering**: $\ell \propto \omega^{-4}$ (Rayleigh)
3. **Umklapp scattering** (high $T$): $\ell \propto e^{\Theta_D/bT}$, $\kappa$ decreases

The result is a characteristic **thermal conductivity peak** at $T \sim \Theta_D/20$.

### Diamond: The Highest Thermal Conductivity

Diamond has the highest $\kappa$ of any bulk material. Inyushkin et al. (2018) measured $\kappa$ of high-purity synthetic single-crystal diamonds from 6 K to 400 K, separating normal and Umklapp phonon-phonon scattering contributions [Inyushkin 2018]:

| $T$ (K) | $\kappa$ (W/m·K) |
|---------|-----------------|
| 6 | 15 |
| 10 | 120 |
| 20 | 2800 |
| 40 | 12000 |
| **80** | **14000** |
| 150 | 4500 |
| 300 | 2200 |
| 400 | 1600 |

*From Inyushkin et al. (2018), Phys. Rev. B 97, 144305.*

The enormous peak at **80 K** ($\kappa = 14\,000$ W/m·K) and subsequent rapid decrease demonstrate Umklapp scattering onset. At room temperature, $\kappa \approx 2200$ W/m·K — still 5× higher than copper.

### Umklapp Processes

In a **normal** (N) process: $\mathbf{q}_1 + \mathbf{q}_2 = \mathbf{q}_3$ (momentum conserved within the zone).

In an **Umklapp** (U) process: $\mathbf{q}_1 + \mathbf{q}_2 = \mathbf{q}_3 + \mathbf{G}$ (a reciprocal lattice vector is needed).

Only U-processes create thermal resistance. Their rate decreases exponentially at low $T$ ($\propto e^{-\Theta_D/bT}$) because they require zone-boundary phonons that are thermally activated.

### Room-Temperature Thermal Conductivity

| Material | $\kappa$ (W/m·K) | Dominant carrier |
|----------|-----------------|-----------------|
| Diamond | 2200 | phonons |
| Cu | 401 | electrons |
| Al | 237 | electrons |
| Si | 148 | phonons |
| Fe | 80 | electrons + phonons |
| GaAs | 46 | phonons |
| NaCl | 7 | phonons |
| Glass (SiO₂) | 1.4 | phonons (localized) |

---

## References

1. **Inyushkin, A. V.** et al. (2018). "Thermal conductivity of high purity synthetic single crystal diamonds." *Phys. Rev. B* **97**, 144305. DOI: [10.1103/PhysRevB.97.144305](https://doi.org/10.1103/PhysRevB.97.144305). — *Diamond κ(T) from 6 K to 400 K. Peak 14000 W/m·K at 80 K.*

2. **Parkinson, D. H.** (1958). "The specific heats of metals at low temperatures." *Rep. Prog. Phys.* **21**, 307. DOI: [10.1088/0034-4885/21/1/307](https://doi.org/10.1088/0034-4885/21/1/307). — *Comprehensive review of metal specific heat with Debye fits.*

3. **Abrahams, S. C.** et al. (1975). "Debye temperatures and cohesive properties." *J. Chem. Phys.* **63**, 1162.

4. **Grimvall, G.** et al. (1974). "Correlation of properties of materials to Debye and melting temperatures." *Phys. Scripta* **10**, 340.
