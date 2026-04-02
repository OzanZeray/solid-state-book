# Chapter 8: Semiconductor Crystals

Semiconductors are the foundation of modern electronics. Their tunable band gaps, controllable carrier concentrations, and high mobilities have enabled the transistor, IC, laser, and solar cell.

---

## 8.1 Effective Mass: Cyclotron Resonance

### The Dresselhaus–Kip–Kittel Experiment (1955)

The most direct measurement of effective mass is **cyclotron resonance**: carriers in a magnetic field orbit at frequency $\omega_c = eB/m^*$. By sweeping the microwave frequency or field, $m^*$ is determined directly.

Dresselhaus, Kip, and Kittel at UC Berkeley performed the definitive cyclotron resonance experiments on Si and Ge at 4 K [Dresselhaus 1955]:

> *"An experimental and theoretical discussion is given of the results of cyclotron resonance experiments on charge carriers in silicon and germanium single crystals near 4°K."* — Dresselhaus, Kip, Kittel, Phys. Rev. 98, 368 (1955)

**Experimental conditions:** Microwave frequencies 9000 and 24,000 MHz; temperature 4 K (liquid helium); magnetic field swept 0–10,000 Oersteds. The condition for observing resonance: $\omega_c\tau \geq 1$, requiring $\tau \approx 10^{-11}$ sec.

**Fig. 2 of the original paper** (p. 372) shows the actual cyclotron resonance absorption spectrum of Ge — distinct peaks for electrons and holes at different magnetic field values.

### Effective Masses (from the abstract, p. 368)

**Germanium** — electron energy surfaces along ⟨111⟩ are prolate spheroids:
- Longitudinal mass: $m_l = (1.58 \pm 0.04) \, m_e$
- Transverse mass: $m_t = (0.082 \pm 0.001) \, m_e$

**Silicon** — electron energy surfaces along ⟨100⟩ are prolate spheroids:
- Longitudinal mass: $m_l = (0.97 \pm 0.02) \, m_e$
- Transverse mass: $m_t = (0.19 \pm 0.01) \, m_e$

The energy surface equation:

$$E(\mathbf{k}) = Ak^2 \pm [B^2k^4 + C^2(k_x^2k_y^2 + k_y^2k_z^2 + k_z^2k_x^2)]^{1/2}$$

with constants (from the abstract):
- **Ge**: $A = -(13.0\pm0.2)\hbar^2/2m$, $|B| = (8.9\pm0.1)\hbar^2/2m$, $|C| = (10.3\pm0.2)\hbar^2/2m$
- **Si**: $A = -(4.1\pm0.2)\hbar^2/2m$, $|B| = (1.6\pm0.2)\hbar^2/2m$, $|C| = (3.3\pm0.5)\hbar^2/2m$

### Complete Effective Mass Table

| Material | $m_l^*/m_e$ | $m_t^*/m_e$ | $m_{hh}^*/m_e$ | $m_{lh}^*/m_e$ | $E_g$ (eV) |
|----------|-----------|-----------|-------------|-------------|-----------|
| Si | **0.97±0.02** | **0.19±0.01** | 0.49 | 0.16 | 1.12 |
| Ge | **1.58±0.04** | **0.082±0.001** | 0.33 | 0.04 | 0.66 |
| GaAs | 0.067 | — | 0.45 | 0.082 | 1.42 |
| InSb | 0.014 | — | 0.40 | 0.016 | 0.24 |

*Bold: directly from Dresselhaus, Kip, Kittel (1955).*

---

## 8.2 Intrinsic Carrier Concentration

$$n_i = \sqrt{N_c N_v} \exp(-E_g / 2k_BT)$$

| Material | $n_i$ at 300 K (cm⁻³) | $E_g$ (eV) |
|----------|---------------------|-----------|
| Si | 1.0 × 10¹⁰ | 1.12 |
| Ge | 2.4 × 10¹³ | 0.66 |
| GaAs | 1.8 × 10⁶ | 1.42 |
| InSb | 1.6 × 10¹⁶ | 0.24 |

The exponential dependence on $E_g/k_BT$ spans 10 orders of magnitude.

## 8.3 Donor and Acceptor Ionization Energies

Dean et al. (1967) measured ionization energies from radiative recombination involving neutral donors and acceptors in Si and Ge [Dean 1967]:

| Type | Impurity | In Si (meV) | In Ge (meV) |
|------|----------|------------|------------|
| Donor | P | 45 | 12.0 |
| Donor | As | 54 | 12.7 |
| Donor | Sb | 39 | 9.6 |
| Acceptor | B | 45 | 10.4 |
| Acceptor | Al | 67 | 10.2 |
| Acceptor | Ga | 72 | 10.8 |
| Acceptor | In | 160 | 11.2 |

*From Dean et al. (1967), Phys. Rev. 161, 711.*

## 8.4 Carrier Mobility

Li and Thurber (1977) measured electron mobility in P-doped Si [Li & Thurber 1977]:

| $N_D$ (cm⁻³) | $\mu_e$ (cm²/V·s) |
|-------------|-------------------|
| 10¹⁴ | 1450 |
| 10¹⁵ | 1350 |
| 10¹⁶ | 1200 |
| 10¹⁷ | 750 |
| 10¹⁸ | 280 |
| 10¹⁹ | 110 |

At low doping: phonon scattering dominates ($\mu \approx 1450$). At high doping: ionized impurity scattering ($\mu$ drops 13×).

---

## References

1. **Dresselhaus, G., Kip, A. F., and Kittel, C.** (1955). "Cyclotron Resonance of Electrons and Holes in Silicon and Germanium Crystals." *Phys. Rev.* **98**, 368–384. DOI: [10.1103/PhysRev.98.368](https://doi.org/10.1103/PhysRev.98.368). — *Effective masses of Si and Ge from cyclotron resonance at 4 K. Fig. 2: actual absorption spectrum.*
2. **Dean, P. J.** et al. (1967). "New radiative recombination processes involving neutral donors and acceptors in silicon and germanium." *Phys. Rev.* **161**, 711. DOI: [10.1103/PhysRev.161.711](https://doi.org/10.1103/PhysRev.161.711).
3. **Li, S. S. and Thurber, W. R.** (1977). "The dopant density and temperature dependence of electron mobility and resistivity in n-type silicon." *Solid-State Electron.* **20**, 609. DOI: [10.1016/0038-1101(77)90100-9](https://doi.org/10.1016/0038-1101(77)90100-9).
