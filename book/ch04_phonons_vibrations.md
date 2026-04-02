# Chapter 4: Phonons I — Crystal Vibrations

The atoms in a crystal vibrate about their equilibrium positions. These vibrations, quantized as *phonons*, determine most thermal, acoustic, and transport properties. This chapter presents the experimental phonon dispersion curves that reveal how lattice vibrations propagate through crystals.

---

## 4.1 Vibrations of Crystals with Monatomic Basis

For a 1D chain of identical atoms (mass $M$, spacing $a$, force constant $C$):

$$\omega(k) = 2\sqrt{\frac{C}{M}}\left|\sin\frac{ka}{2}\right|$$

Key features:
- Long wavelengths ($k \to 0$): $\omega \approx v_s |k|$, where $v_s = a\sqrt{C/M}$
- Zone boundary ($k = \pi/a$): $\omega_{max} = 2\sqrt{C/M}$, group velocity $v_g = 0$
- Periodicity: first Brillouin zone is $-\pi/a < k \leq \pi/a$

---

## 4.2 The First Phonon Dispersion Curve: Brockhouse and Stewart (1955)

The experimental measurement of phonon dispersion relations was made possible by **inelastic neutron scattering**, developed by Bertram Brockhouse at Chalk River, Canada. Brockhouse received the **1994 Nobel Prize in Physics**.

### The Experiment

From the original paper: *"Monoenergetic neutrons provided by a crystal spectrometer (wavelength 1.14₈ Å, energy 0.062₂ ev) were scattered at an angle of 95.1° by an aluminum single crystal."* [Brockhouse & Stewart 1955, p. 757]

The method works by conservation of energy and momentum:

$$E' = E - \hbar\omega_f \quad \text{(energy)}$$

$$\hbar\mathbf{q} = \hbar\mathbf{k} - \hbar\mathbf{k}' - \hbar\mathbf{G} \quad \text{(momentum)}$$

By measuring the energy and direction of scattered neutrons, the phonon frequency $\omega(\mathbf{q})$ is determined.

### Brockhouse's Data: Aluminum Phonon Dispersion

Fig. 3 of Brockhouse & Stewart (1955) shows **the first phonon dispersion curve ever measured** — $\omega$ vs $q$ for aluminum [Brockhouse & Stewart 1955, p. 757]:

- **Longitudinal branch** (open circles): rising to ~6 × 10¹³ rad/sec
- **Transverse branch** (filled circles, near {111} axes): rising to ~3 × 10¹³ rad/sec
- The dashed curve is a sinusoidal fit for a 1D model

The transverse sound velocity extracted from the low-$q$ slope: **$v_T$ = 3080 m/sec**, in agreement with the elastic constants of Chapter 3.

### Precision Measurements: Stedman and Nilsson (1966)

Stedman and Nilsson performed the most precise Al phonon measurements at 80 K and 300 K (204 citations), achieving errors of only ~0.6% [Stedman & Nilsson 1966]. Key findings:
- **Kohn anomalies** in the dispersion curves (abrupt changes caused by electronic screening at $2k_F$)
- **Phonon widths** at 80 K from the electron-phonon interaction
- Force constants extending to 15th neighbors (range: 2.6 lattice spacings)

### Phonon Frequencies at High-Symmetry Points in Aluminum

| Symmetry point | Branch | Frequency (THz) |
|---------------|--------|-----------------|
| $X$ [100] zone boundary | $L$ | 9.69 |
| $X$ [100] zone boundary | $T$ | 5.76 |
| $L$ [111] zone boundary | $L$ | 9.78 |
| $L$ [111] zone boundary | $T$ | 4.48 |
| $K$ [110] zone boundary | $T_1$ | 7.44 |

*From Brockhouse (1958).*

---

## 4.3 Two Atoms per Primitive Basis: NaI

When the primitive cell contains two atoms, the dispersion splits into **acoustic** (atoms in phase) and **optical** (atoms out of phase) branches.

### Woods, Cochran, and Brockhouse (1960): NaI Phonon Dispersion

The landmark demonstration of acoustic and optical branches was by Woods et al. (1960), who measured the complete phonon dispersion of NaI [Woods 1960]. NaI was chosen because the large mass ratio ($M_I/M_{Na} = 127/23 = 5.5$) produces a wide gap between branches.

With 2 atoms per primitive cell: 6 branches total (1 LA + 2 TA + 1 LO + 2 TO).

| Direction | Branch | $\Gamma$ point (THz) | Zone boundary (THz) |
|-----------|--------|---------------------|-------------------|
| [100] | LA | 0 | 2.7 |
| [100] | TA | 0 | 1.8 |
| [100] | LO | 4.5 | 3.8 |
| [100] | TO | 3.6 | 2.1 |

*From Woods et al. (1960), Phys. Rev. 119, 980.*

The **frequency gap** between the acoustic branches (~2.7 THz) and optical branches (~3.6 THz) is clearly visible. Electromagnetic radiation in this range cannot couple to the lattice — the **Reststrahlen band**.

---

## 4.4 Quantization and Phonon Momentum

A phonon has energy $\hbar\omega$ and crystal momentum $\hbar\mathbf{q}$. The mean occupation at temperature $T$:

$$\langle n_{\mathbf{q}s} \rangle = \frac{1}{e^{\hbar\omega/k_BT} - 1}$$

Crystal momentum is defined only modulo $\mathbf{G}$ — this distinction matters for Umklapp processes (Chapter 5).

---

## References

1. **Brockhouse, B. N. and Stewart, A. T.** (1955). "Scattering of Neutrons by Phonons in an Aluminum Single Crystal." *Phys. Rev.* **100**, 756–757. DOI: [10.1103/PhysRev.100.756](https://doi.org/10.1103/PhysRev.100.756). — *The first phonon dispersion curve ever measured. Contains Fig. 3 showing ω vs q for Al with transverse sound velocity 3080 m/sec.*

2. **Brockhouse, B. N.** (1958). "Normal Modes of Aluminum by Neutron Spectrometry." *Rev. Mod. Phys.* **30**, 236. DOI: [10.1103/RevModPhys.30.236](https://doi.org/10.1103/RevModPhys.30.236).

3. **Woods, A. D. B., Cochran, W., and Brockhouse, B. N.** (1960). "Lattice Dynamics of Alkali Halide Crystals." *Phys. Rev.* **119**, 980–999. DOI: [10.1103/PhysRev.119.980](https://doi.org/10.1103/PhysRev.119.980). — *NaI phonon dispersion showing acoustic + optical branches. 654 citations.*

4. **Woods, A. D. B.** et al. (1963). "Lattice Dynamics of Alkali Halide Crystals. II." *Phys. Rev.* **131**, 1025. DOI: [10.1103/PhysRev.131.1025](https://doi.org/10.1103/PhysRev.131.1025).

5. **Stedman, R. and Nilsson, G.** (1966). "Dispersion Relations for Phonons in Aluminum at 80 and 300 K." *Phys. Rev.* **145**, 492. DOI: [10.1103/PhysRev.145.492](https://doi.org/10.1103/PhysRev.145.492). — *Precision Al phonon data. 204 citations.*

6. **Kresch, M.** et al. (2008). "Phonons in aluminum at high temperatures studied by inelastic neutron scattering." *Phys. Rev. B* **77**, 024301. — *Al phonon DOS at 10, 150, 300, 525, 775 K.*
