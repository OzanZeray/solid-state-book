# Chapter 2: Wave Diffraction and the Reciprocal Lattice

The determination of crystal structures is an experimental science. The primary tool is the diffraction of waves — X-rays, neutrons, or electrons — by the periodic arrangement of atoms in a crystal. In this chapter we present the experimental foundations: the Bragg law, the reciprocal lattice, the structure factor, and the landmark diffraction experiments that established our understanding of crystal structure and wave-particle duality.

---

## 2.1 Diffraction of Waves by Crystals

### 2.1.1 Bragg Law

In 1912, Max von Laue suggested that X-rays, with wavelengths comparable to interatomic spacings (~1 Å), should be diffracted by crystals. The experiment was performed by Friedrich and Knipping, producing the first X-ray diffraction pattern from a crystal of copper sulfate.

The following year, W. L. Bragg provided the simple geometric interpretation [Bragg 1913]. Consider a set of parallel lattice planes with spacing $d$. An X-ray beam incident at angle $\theta$ to the planes is reflected specularly from each plane. Constructive interference occurs when:

$$2d\sin\theta = n\lambda$$

This is the **Bragg law** — the single most important equation in crystallography.

### Bragg's Original Verification (1913)

Bragg verified this law by analyzing diffraction from alkali halides. His key experimental observations (from Tables II–IX of the original paper):

- **KCl**: All reflections present → appears as simple cubic (because K⁺ and Cl⁻ are isoelectronic with 18 electrons each)
- **KBr**: Only reflections with all-odd or all-even $(hkl)$ → fcc selection rule (because K = 39, Br = 80 differ strongly in scattering power)
- **NaCl**: Intermediate behavior → both sublattices visible but with different intensities (Na = 23, Cl = 35.5)

> *"In the case of potassium chloride the atoms of potassium and chlorine, of atomic weight 39 and 35.5 respectively, are sufficiently close in atomic weight to act as identical diffracting centres."* — Bragg 1913, p. 264

### 2.1.2 The Debye–Scherrer Powder Method

In 1916, Debye and Scherrer demonstrated that crystalline powders also produce useful diffraction patterns. Because a powder contains crystallites in all orientations, each set of planes $(hkl)$ produces a diffraction cone of half-angle $2\theta$, forming rings on a detector.

The powder method is the most widely used technique for routine crystal identification. Each material produces a unique "fingerprint" of $d$-spacings and intensities, catalogued in the Powder Diffraction File (PDF) database containing over 1,000,000 entries.

**Example: Aluminum powder XRD** (Cu Kα, λ = 1.5406 Å):

| $(hkl)$ | $2\theta$ (deg) | $d$ (Å) | Relative Intensity |
|---------|----------------|---------|-------------------|
| (111) | 38.47 | 2.338 | very strong |
| (200) | 44.74 | 2.024 | strong |
| (220) | 65.13 | 1.431 | medium |
| (311) | 78.23 | 1.221 | medium |
| (222) | 82.43 | 1.169 | weak |

The fcc selection rule (reflections only when $h,k,l$ are all odd or all even) is directly confirmed.

---

## 2.2 Reciprocal Lattice

The reciprocal lattice vectors are:

$$\mathbf{b}_1 = 2\pi \frac{\mathbf{a}_2 \times \mathbf{a}_3}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}, \quad \mathbf{b}_2 = 2\pi \frac{\mathbf{a}_3 \times \mathbf{a}_1}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}, \quad \mathbf{b}_3 = 2\pi \frac{\mathbf{a}_1 \times \mathbf{a}_2}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}$$

The Bragg condition is equivalent to the **Laue condition**: diffraction occurs when the scattering vector $\Delta\mathbf{k} = \mathbf{k}' - \mathbf{k}$ equals a reciprocal lattice vector $\mathbf{G}$.

**Key results:**
- The reciprocal of sc (side $a$) is sc (side $2\pi/a$)
- The reciprocal of bcc is fcc, and vice versa
- The first Brillouin zone is the Wigner–Seitz cell of the reciprocal lattice

---

## 2.3 Structure Factor

The intensity of a diffracted beam is proportional to $|S_\mathbf{G}|^2$, where:

$$S_\mathbf{G} = \sum_j f_j \, e^{-i\mathbf{G} \cdot \mathbf{r}_j}$$

### Structure Factor of the bcc Lattice

With atoms at $(0,0,0)$ and $(1/2, 1/2, 1/2)$:

$$S_{hkl} = f[1 + e^{-i\pi(h+k+l)}] = \begin{cases} 2f & \text{if } h+k+l \text{ even} \\ 0 & \text{if } h+k+l \text{ odd} \end{cases}$$

### Structure Factor of the fcc Lattice

$$S_{hkl} = \begin{cases} 4f & \text{if } h,k,l \text{ all odd or all even} \\ 0 & \text{otherwise (mixed)} \end{cases}$$

These selection rules are the theoretical explanation for what Bragg observed experimentally in 1913: the systematic absences in KBr (fcc) vs. the complete pattern in KCl (appears sc).

### Atomic Form Factor

The atomic form factor $f(\sin\theta/\lambda)$ equals the number of electrons $Z$ at $\theta = 0$ and decreases with scattering angle. Hubbell et al. (1975) tabulated form factors for all elements $Z = 1$ to 100 — one of the most cited works in X-ray physics with **1678 citations** [Hubbell 1975].

| Atom | $s = 0$ | $s = 0.25$ Å⁻¹ | $s = 0.50$ Å⁻¹ | $s = 1.00$ Å⁻¹ |
|------|---------|----------------|----------------|----------------|
| C ($Z=6$) | 6.0 | 4.1 | 2.3 | 0.9 |
| Na ($Z=11$) | 11.0 | 7.8 | 4.7 | 2.0 |
| Cl ($Z=17$) | 17.0 | 12.4 | 7.8 | 3.5 |
| Cu ($Z=29$) | 29.0 | 22.5 | 15.2 | 7.4 |
| Ge ($Z=32$) | 32.0 | 25.1 | 17.2 | 8.5 |

---

## 2.4 Neutron Diffraction

Neutrons with wavelengths ~1 Å at thermal energies ($E \approx 25$ meV) are also diffracted by crystals. However, neutrons scatter from *nuclei* rather than electron clouds, giving complementary information.

### Shull and Wollan: Pioneers of Neutron Diffraction

Clifford Shull and Ernest Wollan at Oak Ridge National Laboratory developed neutron diffraction in the late 1940s, using neutron beams from the X-10 graphite reactor built during the Manhattan Project.

Their landmark results:

- **1948**: First neutron powder diffraction patterns, determining coherent neutron scattering lengths for many elements [Wollan & Shull 1948].
- **1949**: Structure of ice by neutron diffraction — locating hydrogen atoms invisible to X-rays.
- **1951**: First experimental evidence of **antiferromagnetic order in MnO** — magnetic Bragg peaks below the Néel temperature absent in X-ray diffraction [Shull, Strauser & Wollan 1951]. This paper has **1321 citations**.

Shull described the early days in his 1995 Nobel lecture: *"I would like to express... my deep regret that Ernest Wollan, who first guided me to the wonders of neutron-scattering, could not have shared these experiences."* [Shull 1995, p. 753]

Shull received the **1994 Nobel Prize in Physics** "for the development of the neutron diffraction technique." Wollan had died in 1984.

**Advantages of neutrons over X-rays:**
1. Locate light atoms (H, Li, O) near heavy atoms
2. Distinguish neighboring elements (Mn vs Fe)
3. Detect magnetic order through neutron magnetic moment interaction

---

## 2.5 Electron Diffraction: The Davisson–Germer Experiment (1927)

In one of the most important experiments of the 20th century, Clinton Davisson and Lester Germer at Bell Labs demonstrated the wave nature of electrons by observing their diffraction from a nickel crystal [Davisson & Germer 1927].

### The Experiment

The experiment was partly accidental. While studying electron scattering from polycrystalline nickel in 1925, a liquid air bottle exploded in their laboratory, breaking the vacuum system. The nickel target oxidized. When heated to remove the oxide, the polycrystalline nickel recrystallized into a few large single crystals. When they resumed scattering measurements, they observed sharp diffraction peaks.

From the original 1927 *Nature* paper:

> *"In a series of experiments now in progress, we are directing a narrow beam of electrons normally against a target cut from a single crystal of nickel, and are measuring the intensity of scattering... in various directions in front of the target."* — Davisson & Germer, Nature 119, 558 (1927)

### The Key Data

Davisson and Germer's Figure 2 (p. 559) shows the intensity of electron scattering versus azimuth angle at 54 volts and co-latitude 50°. Three sharp spurs appear at 120° intervals, confirming the threefold symmetry of the Ni(111) surface.

> *"The spurs are due to beams of scattered electrons which are nearly if not quite as well defined as the primary beam."* — Davisson & Germer 1927, p. 558

Their Table I provides the quantitative verification of de Broglie's wave hypothesis. For the {111} azimuth:

| Voltage (V) | Co-latitude θ | Electron speed v (10⁸ cm/s) | $n\lambda$ (Å) | $n(\lambda mv/h)$ |
|------------|--------------|---------------------------|--------------|-----------------|
| 54 | 50° | 4.36 | 1.65 | **0.99** |
| 100 | 31° | 5.94 | 1.11 | **0.91** |
| 174 | 21° | 7.84 | 0.77 | **0.83** |

For the {100} azimuth:

| Voltage (V) | Co-latitude θ | Electron speed v (10⁸ cm/s) | $n\lambda$ (Å) | $n(\lambda mv/h)$ |
|------------|--------------|---------------------------|--------------|-----------------|
| 65 | 44° | 4.79 | 1.49 | **0.98** |
| 126 | 29° | 6.67 | 1.04 | **0.95** |
| 190 | 20° | 8.19 | 0.74 | **0.83** |

The last column $n(\lambda mv/h)$ should equal an integer if the de Broglie relation $\lambda = h/mv$ holds. The values cluster near **1.0** — direct experimental proof that electrons behave as waves with wavelength $\lambda = h/mv$.

The plane spacings used in the analysis were:
- {111} and {100}: $d = 2.15 \times 10^{-8}$ cm
- {110}: $d = 1.24 \times 10^{-8}$ cm

Davisson and Germer noted: *"These results are highly suggestive, of course, of the ideas underlying the theory of wave mechanics."*

This experiment confirmed de Broglie's 1924 hypothesis. De Broglie received the **1929 Nobel Prize**; Davisson shared the **1937 Nobel Prize** with G. P. Thomson.

---

## References

1. **Bragg, W. L.** (1913). "The Structure of Some Crystals as Indicated by Their Diffraction of X-rays." *Proc. R. Soc. Lond. A* **89**, 248–277. DOI: [10.1098/rspa.1913.0083](https://doi.org/10.1098/rspa.1913.0083).

2. **Davisson, C. and Germer, L. H.** (1927). "The Scattering of Electrons by a Single Crystal of Nickel." *Nature* **119**, 558–560. DOI: [10.1038/119558a0](https://doi.org/10.1038/119558a0). — *The paper that proved the wave nature of electrons. Contains Fig. 1 (scattering setup), Fig. 2 (diffraction peaks at 54V), and Table I with the de Broglie verification data.*

3. **Shull, C. G., Strauser, W. A., and Wollan, E. O.** (1951). "Neutron Diffraction by Paramagnetic and Antiferromagnetic Substances." *Phys. Rev.* **83**, 333–345. DOI: [10.1103/PhysRev.83.333](https://doi.org/10.1103/PhysRev.83.333). — *First neutron diffraction evidence of antiferromagnetic order in MnO. 1321 citations.*

4. **Shull, C. G.** (1995). "Early Development of Neutron Scattering." *Rev. Mod. Phys.* **67**, 753–757. DOI: [10.1103/RevModPhys.67.753](https://doi.org/10.1103/RevModPhys.67.753). — *Nobel Prize lecture.*

5. **Wollan, E. O. and Shull, C. G.** (1948). "The Diffraction of Neutrons by Crystalline Powders." *Phys. Rev.* **73**, 830. DOI: [10.1103/PhysRev.73.830](https://doi.org/10.1103/PhysRev.73.830). — *First neutron powder diffraction.*

6. **Hubbell, J. H.** et al. (1975). "Atomic Form Factors, Incoherent Scattering Functions, and Photon Scattering Cross Sections." *J. Phys. Chem. Ref. Data* **4**, 471–538. DOI: [10.1063/1.555523](https://doi.org/10.1063/1.555523). — *Form factors for Z = 1–100. 1678 citations.*

7. **Pope, C. G.** (1997). "X-ray Diffraction and the Bragg Equation." *J. Chem. Educ.* **74**, 129. DOI: [10.1021/ed074p129](https://doi.org/10.1021/ed074p129). — *Pedagogical derivation of the Bragg equation.*
