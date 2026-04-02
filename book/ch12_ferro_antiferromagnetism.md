# Chapter 12: Ferromagnetism and Antiferromagnetism

In ferromagnets, neighboring moments align parallel producing spontaneous magnetization below the Curie temperature. In antiferromagnets, they align antiparallel.

---

## 12.1 Ferromagnetic Elements

| Element | $T_C$ (K) | $M_s(0)$ (kA/m) | $\mu/\mu_B$ | Structure |
|---------|----------|----------------|------------|-----------|
| Fe | 1043 | 1752 | 2.22 | bcc |
| Co | 1394 | 1446 | 1.72 | hcp |
| Ni | 631 | 510 | 0.60 | fcc |
| Gd | 293 | 2060 | 7.63 | hcp |

Non-integer moments (2.22, 1.72, 0.60 $\mu_B$) evidence itinerant ferromagnetism.

## 12.2 Bloch $T^{3/2}$ Law: Rode & Herrmann (1964)

Rode and Herrmann measured $\Delta I(T)$ of Fe, Co, Ni at 4.2–70 K in 20 kOe fields [Rode & Herrmann 1964]. Data extracted directly from the Soviet Physics JETP paper:

**Iron $\Delta I(T)$ at $H = 20$ kOe:**

| $T$ (K) | $\Delta I$ (G) | $T$ (K) | $\Delta I$ (G) |
|---------|-------------|---------|-------------|
| 4.2 | 0 | 25.0 | 0.90 |
| 5.4 | 0.03 | 27.6 | 1.05 |
| 7.1 | 0.08 | 30.4 | 1.24 |
| 9.0 | 0.15 | 34.9 | 1.53 |
| 10.0 | 0.19 | 40.0 | 1.84 |
| 12.0 | 0.27 | 44.8 | 2.22 |
| 13.5 | 0.34 | 49.1 | 2.58 |
| 15.9 | 0.44 | 53.4 | 2.95 |
| 18.0 | 0.54 | 61.0 | 3.50 |
| 21.8 | 0.76 | | |

*From Rode & Herrmann, JETP 19(5), 1081 (1964), Table II.*

Bloch law: $\Delta I/I_0 = cT^{3/2}$. Fitted coefficients:

| Metal | $c \times 10^6$ | Exchange integral $A$ (erg) |
|-------|---------------|--------------------------|
| Fe | 4.5 ± 0.1 | $(1.59 \pm 0.05) \times 10^{-14}$ |
| Co | 2.4 ± 0.1 | $(2.92 \pm 0.05) \times 10^{-14}$ |
| Ni | 9.3 ± 0.25 | $(2.3 \pm 0.04) \times 10^{-14}$ |

Nickel deviates from $T^{3/2}$ above 30 K, requiring: $\Delta I/I_0 = cT^{3/2} + dT^{5/2}e^{-\Delta/k_BT}$ with $\Delta/k_B = 98 \pm 4$ K — evidence for a magnon spectrum gap.

## 12.3 Antiferromagnetic Order: Shull (1951)

Shull, Strauser, and Wollan provided the first experimental proof of AFM order by observing magnetic Bragg peaks in MnO below 120 K [Shull 1951]. This paper has **1321 citations**.

| Material | $T_N$ (K) | Structure |
|----------|----------|-----------|
| MnO | 116 | NaCl (AFM type II) |
| MnF₂ | 67 | rutile |
| FeO | 198 | NaCl |
| NiO | 525 | NaCl |
| CoO | 291 | NaCl |
| Cr | 311 | bcc (SDW) |

## 12.4 Hysteresis

| Material | $B_r$ (T) | $H_c$ (kA/m) | Type |
|----------|----------|-------------|------|
| Fe (annealed) | 1.3 | 0.08 | very soft |
| Permalloy | 0.6 | 0.004 | very soft |
| Alnico 5 | 1.27 | 50 | hard |
| Nd₂Fe₁₄B | 1.28 | 880 | very hard |
| SmCo₅ | 0.92 | 720 | very hard |

Coercive field spans 5 orders of magnitude.

---

## References

1. **Rode, V. E. and Herrmann, R.** (1964). "Investigation of the Magnetization of Iron, Cobalt, and Nickel at Low Temperatures." *JETP* **19**(5), 1081–1083. — *Fe/Co/Ni ΔI(T) data at 20 kOe, Bloch T^{3/2} coefficients.*
2. **Shull, C. G., Strauser, W. A., and Wollan, E. O.** (1951). "Neutron Diffraction by Paramagnetic and Antiferromagnetic Substances." *Phys. Rev.* **83**, 333. DOI: [10.1103/PhysRev.83.333](https://doi.org/10.1103/PhysRev.83.333). — *1321 citations.*
3. **Lynn, J. W.** et al. (1984). "Neutron scattering study of the magnon energies in iron at high energy transfers." *J. Appl. Phys.* **55**, 2Sr. DOI: [10.1063/1.333481](https://doi.org/10.1063/1.333481). — *Fe spin waves to 160 meV.*
