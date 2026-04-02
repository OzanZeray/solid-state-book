# Chapter 13: Magnetic Resonance

Magnetic resonance techniques exploit the interaction of electromagnetic radiation with magnetic moments in solids. Nuclear magnetic resonance (NMR), electron paramagnetic resonance (EPR), and ferromagnetic resonance (FMR) provide detailed information about local electronic structure, bonding, and magnetic order.

---

## 13.1 Nuclear Magnetic Resonance

### Discovery

In 1946, Edward Purcell at Harvard and Felix Bloch at Stanford independently detected NMR signals from bulk matter — Purcell from paraffin wax, Bloch from water. They shared the **1952 Nobel Prize in Physics**.

As Alloul (2015, arXiv:1504.06992) describes: *"Discovered at the outset of the second world War by F. Bloch and E.M. Purcell, the nuclear magnetic resonance technique has become quite immediately a unique method to investigate the chemical and physical properties of condensed matter."*

### The Resonance Condition

A nucleus with spin $I$ in a magnetic field $B_0$ has $2I+1$ energy levels separated by:

$$\Delta E = \hbar \gamma_n B_0$$

where $\gamma_n$ is the gyromagnetic ratio. Resonant absorption occurs at the **Larmor frequency**:

$$\nu_L = \gamma_n B_0 / 2\pi$$

### NMR Properties of Common Nuclei

| Nucleus | Spin $I$ | $\gamma_n/2\pi$ (MHz/T) | Natural Abundance (%) | Relative Sensitivity |
|---------|----------|--------------------------|----------------------|---------------------|
| ¹H | 1/2 | 42.58 | 99.99 | 1.000 |
| ¹³C | 1/2 | 10.71 | 1.11 | 0.016 |
| ¹⁹F | 1/2 | 40.08 | 100 | 0.833 |
| ²³Na | 3/2 | 11.27 | 100 | 0.093 |
| ²⁷Al | 5/2 | 11.09 | 100 | 0.207 |
| ²⁹Si | 1/2 | 8.47 | 4.70 | 0.008 |
| ⁵¹V | 7/2 | 11.21 | 99.76 | 0.383 |
| ⁶³Cu | 3/2 | 11.29 | 69.1 | 0.093 |

> **Reference:** Alloul, H. (2015). "NMR studies of electronic properties of solids." Scholarpedia 9(9):32069. arXiv:1504.06992.

---

## 13.2 Knight Shift

In metals, the NMR resonance frequency is shifted from the free-nucleus value by the **Knight shift** $K$, arising from the contact interaction between the nuclear spin and the conduction electron spin density at the nucleus:

$$K = \frac{A_0 \chi_{P0}}{g \mu_B \hbar \gamma_n}$$

where $A_0$ is the contact hyperfine coupling constant and $\chi_{P0} = (g\mu_B)^2 \rho(E_F)/2$ is the Pauli spin susceptibility, directly measuring the electronic density of states at the Fermi level.

The Knight shift is "usually a large quantity which is measured in %. This comes about because the contact coupling $A_0$ is usually much larger than the corresponding dipole or orbital couplings" (Alloul 2015).

### Experimental Knight Shift Values

| Metal | $K$ (%) | Metal | $K$ (%) |
|-------|---------|-------|---------|
| Li | 0.026 | Cu | 0.237 |
| Na | 0.112 | Al | 0.162 |
| K | 0.265 | Pt | 2.90 |
| Rb | 0.653 | Sn | 0.73 |

The Knight shift increases with the Pauli susceptibility and the $s$-electron density at the nucleus.

---

## 13.3 Spin-Lattice Relaxation and the Korringa Relation

The spin-lattice relaxation time $T_1$ measures how quickly the nuclear spin system reaches thermal equilibrium with the lattice. In a simple metal:

$$(T_1 T)^{-1} = \frac{\pi k_B A_0^2 \rho^2(E_F)}{\hbar}$$

Combining with the Knight shift yields the **Korringa relation**:

$$K^2 T_1 T = \frac{\hbar}{4\pi k_B} \left(\frac{g\mu_B}{\hbar \gamma_n}\right)^2$$

### Experimental Verification: ²⁷Al in Aluminum

Alloul (2015) presents data showing that $T_1 T$ of ²⁷Al is constant in pure aluminum over more than **three orders of magnitude** in temperature:

$$T_1 T = 1.85 \text{ sec·K}$$

This remarkable constancy validates the Korringa relation and confirms that aluminum is a well-behaved free-electron metal.

> **Figure description (from arXiv:1504.06992, Fig. 1):** "The ²⁷Al spin lattice relaxation time $T_1$ measured in pure aluminium metal is plotted versus temperature in a log/log scale. The linear fit represents the relation $T_1 T = 1.85$ sec·K."

### Deviations from the Korringa Relation

In nearly ferromagnetic metals (e.g., TiBe₂, Pd), the Stoner enhancement factor $S = 1/(1 - I\chi_{P0})$ modifies the Korringa relation. The Knight shift is more enhanced than $(T_1 T)^{-1}$ because the enhancement is peaked at $\mathbf{q} = 0$.

In nearly antiferromagnetic metals (e.g., MnSi), the opposite occurs: $\chi(\mathbf{q})$ is peaked at the AF wavevector, and the Korringa constant is *decreased*.

---

## 13.4 NMR in Superconductors

### Knight Shift Suppression Below Tc

In a BCS superconductor, the pairing of electrons in singlet states suppresses the spin susceptibility. The Knight shift decreases below $T_c$ following the **Yosida function**:

$$\frac{K_s(T)}{K_n} = \int_\Delta^\infty \frac{|E|}{(E^2 - \Delta^2)^{1/2}} \left(-\frac{df}{dE}\right) dE$$

> **Experimental example (from arXiv:1504.06992, Fig. 2):** "The ¹⁵⁵Cs and ¹³C NMR shifts measured in the Cs₃C₆₀ phase are plotted versus $T$ below the superconducting temperature $T_c = 30$ K. The NMR shifts follow the standard Yosida type decrease expected for singlet superconductivity." — Wzietek et al., Phys. Rev. Lett. 112, 066401 (2014).

### Hebel-Slichter Coherence Peak

Below $T_c$, the spin-lattice relaxation rate first *increases* above the normal-state Korringa value before decreasing at lower temperatures. This **coherence peak** (Hebel and Slichter, 1957) results from the enhanced density of states piling up above the superconducting gap.

> **Experimental example (from arXiv:1504.06992, Fig. 3):** "The $\log(1/T_1)$ of ⁵¹V in V₃Sn is plotted versus $1/T$ for three distinct applied fields. Below $T_c$ the reduction of $T_1$ represents the Hebel-Slichter coherence peak. At low $T$ all curves point towards an activated behavior associated with the full opening of the superconducting gap." — Adapted from MacLaughlin (1976).

---

## 13.5 Quadrupole Interactions and NQR

Nuclei with $I > 1/2$ have a non-spherical charge distribution (quadrupole moment $Q$) that interacts with the electric field gradient (EFG) at the nuclear site. This splits the NMR spectrum into satellite lines.

### Nuclear Quadrupole Resonance (NQR)

In zero applied field, the quadrupole interaction alone splits the spin levels. For $I = 3/2$:

$$\nu_{NQR} = \nu_Q \sqrt{1 + \eta^2/3}$$

where $\nu_Q$ is the quadrupole frequency and $\eta$ is the asymmetry parameter.

> **Experimental example:** In Na₂/₃CoO₂, the ²³Na NQR spectrum displays three independent NQR lines corresponding to three distinct Na lattice sites, confirming the ordered Na pattern. — Platova et al., Phys. Rev. B 80, 224106 (2009).

---

## 13.6 Electron Paramagnetic Resonance

EPR (also called ESR) detects unpaired electron spins. The resonance condition is:

$$h\nu = g \mu_B B_0$$

### F Centers in Alkali Halides

Holton et al. (1962) measured the EPR spectra of **F centers** (electrons trapped at anion vacancies) in KCl. The F center is a single electron in a roughly spherical potential well formed by the surrounding cations.

**Experimental observations:**
- Single resonance line near $g = 2.001$ (close to the free electron value)
- Hyperfine structure from interaction with neighboring nuclear spins (⁶ nearest K neighbors for KCl)
- Line broadening due to spin-spin interactions between F centers

> **Reference:** Holton, W.C. et al. (1962). "Paramagnetic Resonance of F Centers in Alkali Halides." Phys. Rev. 125, 89. (211 citations)

### Donor Atoms in Silicon

Feher (1959) performed the classic EPR study of phosphorus donors in silicon, observing:
- A doublet due to hyperfine interaction with the ³¹P nucleus ($I = 1/2$)
- The splitting gives the electron density at the P nucleus: $|\psi(0)|^2$
- g-factor anisotropy reflecting the ellipsoidal conduction band minima

---

## 13.7 Ferromagnetic Resonance

In ferromagnetic resonance (FMR), the entire magnetization of a sample precesses coherently around the applied field. For an ellipsoidal sample:

$$\omega = \gamma \sqrt{(B_0 + (N_x - N_z)M_s)(B_0 + (N_y - N_z)M_s)}$$

where $N_x, N_y, N_z$ are demagnetization factors.

For a thin film magnetized in-plane: $\omega = \gamma \sqrt{B_0(B_0 + \mu_0 M_s)}$ (Kittel formula).

### Spin Wave Resonance

In a thin ferromagnetic film, standing spin waves can be excited, producing additional resonance lines at fields below the uniform FMR mode:

$$B_n = B_0 - \frac{D n^2 \pi^2}{g \mu_B d^2}$$

where $D$ is the spin-wave stiffness and $d$ is the film thickness.

---

## 13.8 RKKY Oscillations Observed by NMR

One of the most striking demonstrations of NMR as a local probe is the direct observation of **RKKY spin density oscillations** around magnetic impurities in metals.

In dilute Cu-Mn alloys, Alloul (2012) resolved up to **17 distinct shells** of Cu neighbors around each Mn impurity, each with a different Knight shift. The spatial dependence follows:

$$\Delta K(R_n) \propto \frac{\cos(2k_F R_n)}{R_n^3} \langle S_z \rangle$$

> **Figure description (from arXiv:1504.06992, Fig. 5):** "NMR spectra of the ⁶³Cu and ⁶⁵Cu nuclear spins in dilute Cu-Mn alloys obtained by sweeping the applied external field, at 1.3 K. On both sides of the central lines one can see the weak NMR signals of the diverse copper shells of neighbors."

> **Reference:** Alloul, H. (2012). "From Friedel oscillations and Kondo effect to the pseudogap in cuprates." J. Supercond. Nov. Mag. 25, 385. arXiv:1204.3804.

---

## References

1. Alloul, H. (2015). "NMR studies of electronic properties of solids." Scholarpedia 9(9):32069. **arXiv:1504.06992** — *Primary source for this chapter*
2. Holton, W.C. et al. (1962). "Paramagnetic Resonance of F Centers in Alkali Halides." Phys. Rev. 125, 89.
3. Hebel, L.C. and Slichter, C.P. (1957). "Nuclear Spin Relaxation in Normal and Superconducting Aluminum." Phys. Rev. 113, 1504.
4. MacLaughlin, D.E. (1976). "Magnetic Resonance in the Superconducting State." Solid State Physics 31, 1.
5. Wzietek, P. et al. (2014). "NMR study of the Superconducting gap variation near the Mott transition in Cs₃C₆₀." Phys. Rev. Lett. 112, 066401.
6. Alloul, H. (2012). "From Friedel oscillations and Kondo effect to the pseudogap in cuprates." J. Supercond. Nov. Mag. 25, 385. arXiv:1204.3804.
7. Platova, T.A. et al. (2009). "NQR and X-ray investigation of the structure of Na₂/₃CoO₂." Phys. Rev. B 80, 224106.
8. Abragam, A. (1961). *The Principles of Nuclear Magnetism*. Oxford: Clarendon Press.
9. Slichter, C.P. (1963). *Principles of Magnetic Resonance*. Harper and Row (3rd ed. 1989, Springer).
