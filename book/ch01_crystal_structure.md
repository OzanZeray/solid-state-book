# Chapter 1: Crystal Structure

An ideal crystal is constructed by the infinite repetition of identical groups of atoms. A group is called the *basis*. The set of mathematical points to which the basis is attached is called the *lattice*. The lattice is a periodic array of points in space; the basis is what sits on each point.

---

## 1.1 Periodic Array of Atoms

A lattice is defined by three fundamental translation vectors **a₁**, **a₂**, **a₃** such that any lattice point **R** can be written as:

$$\mathbf{R} = n_1 \mathbf{a}_1 + n_2 \mathbf{a}_2 + n_3 \mathbf{a}_3$$

where $n_1, n_2, n_3$ are integers.

As W. L. Bragg wrote in 1913: *"In treating the diffraction of waves by a space point system such as a crystal, that case is the most simple in which the diffraction is caused by a series of points arranged in a space lattice, of one of the 14 Bravais types. Here every point is identical with every other point of the arrangement, and it is always possible to find an element of the pattern consisting of a parallelepiped with a point at each corner."* [Bragg 1913, p. 249]

The crystal structure is then given by specifying the lattice and the basis. The same lattice can describe very different crystals if the basis is changed.

## 1.2 Fundamental Types of Lattices

In two dimensions there are exactly 5 distinct lattice types. In three dimensions, Auguste Bravais showed in 1848 that there are exactly **14 distinct lattice types**, classified into 7 crystal systems.

| System | Axes | Angles | Bravais Lattices |
|--------|------|--------|-----------------|
| Cubic | a = b = c | α = β = γ = 90° | sc, bcc, fcc |
| Tetragonal | a = b ≠ c | α = β = γ = 90° | simple, body-centered |
| Orthorhombic | a ≠ b ≠ c | α = β = γ = 90° | simple, base, body, face |
| Hexagonal | a = b ≠ c | α = β = 90°, γ = 120° | simple |
| Trigonal | a = b = c | α = β = γ ≠ 90° | simple |
| Monoclinic | a ≠ b ≠ c | α = γ = 90° ≠ β | simple, base-centered |
| Triclinic | a ≠ b ≠ c | α ≠ β ≠ γ | simple |

### Index System for Crystal Planes (Miller Indices)

A crystal plane is specified by three integers $(hkl)$, the Miller indices. The plane makes intercepts $a/h$, $b/k$, $c/l$ on the crystal axes.

Bragg introduced these to X-ray crystallography in his 1913 paper (where he called them "Millerian indices"): *"There can be assigned to each set of parallel planes integral indices $(h, k, l)$... Here the integers $h, k, l$, are reciprocal to the intercepts which a parallel plane makes on the axis of reference."* [Bragg 1913, p. 250]

---

## 1.3 Simple Crystal Structures

### Experimentally Measured Lattice Parameters

The data in the table below are from X-ray diffraction measurements accumulated over more than a century of crystallography, beginning with Bragg's 1913 determination of the NaCl structure.

| Crystal | Structure Type | $a$ (Å) | Source |
|---------|---------------|---------|--------|
| NaCl | Rock salt (B1) | 5.640 | X-ray diffraction |
| KCl | Rock salt (B1) | 6.293 | X-ray diffraction |
| LiF | Rock salt (B1) | 4.027 | X-ray diffraction |
| MgO | Rock salt (B1) | 4.211 | X-ray diffraction |
| CsCl | Cesium chloride (B2) | 4.123 | X-ray diffraction |
| CsBr | Cesium chloride (B2) | 4.286 | X-ray diffraction |
| C (diamond) | Diamond (A4) | 3.567 | X-ray diffraction |
| Si | Diamond (A4) | 5.431 | X-ray diffraction |
| Ge | Diamond (A4) | 5.658 | X-ray diffraction |
| GaAs | Zinc blende (B3) | 5.653 | X-ray diffraction |
| ZnS | Zinc blende (B3) | 5.409 | X-ray diffraction |
| InSb | Zinc blende (B3) | 6.479 | X-ray diffraction |
| Cu | fcc (A1) | 3.615 | X-ray diffraction |
| Al | fcc (A1) | 4.050 | X-ray diffraction |
| Au | fcc (A1) | 4.078 | X-ray diffraction |
| Fe | bcc (A2) | 2.867 | X-ray diffraction |
| W | bcc (A2) | 3.165 | X-ray diffraction |
| Na | bcc (A2) | 4.225 | X-ray diffraction |

---

### 1.3.1 Sodium Chloride Structure

The sodium chloride structure (Strukturbericht designation B1, space group $Fm\bar{3}m$) consists of two interpenetrating fcc lattices of Na⁺ and Cl⁻ ions, displaced by half a lattice parameter along each axis.

**This was the very first crystal structure ever determined.** In his 1913 paper, W. L. Bragg analyzed the X-ray diffraction patterns of NaCl, KCl, KBr, and KI, comparing them systematically to deduce the arrangement of atoms [Bragg 1913].

#### Bragg's Original Argument (1913)

Bragg's reasoning, extracted directly from his paper, proceeded as follows:

1. **KCl appears as a simple cubic lattice.** The diffraction pattern of KCl shows a complete set of spots for all integer indices — as expected for a simple cubic lattice. This is because K⁺ and Cl⁻ are *isoelectronic* (both have 18 electrons), so they scatter X-rays almost identically. As Bragg wrote: *"In the case of potassium chloride the atoms of potassium and chlorine, of atomic weight 39 and 35.5 respectively, are sufficiently close in atomic weight to act as identical diffracting centres."* [Bragg 1913, p. 264]

2. **KBr shows an fcc pattern.** In KBr, the atomic weights differ more (K = 39, Br = 80), and the diffraction pattern shows the characteristic fcc selection rule: only reflections with all-odd or all-even $(hkl)$ are present. Bragg's Tables II and III (p. 257) show this directly — the KBr pattern has systematic absences that the ZnS pattern does not.

3. **NaCl is intermediate.** The NaCl pattern (Tables VII-IX, p. 263) at thin crystal sections (1 mm) resembles KCl, but at thicker sections (6 mm) resembles KBr. This is because Na (atomic weight 23) and Cl (atomic weight 35.5) differ enough to produce different scattering amplitudes for the two sublattices.

4. **The structure.** Bragg deduced that in all alkali halides, the atoms are arranged on two interpenetrating fcc lattices (Fig. 10, p. 265). He provided three rules [Bragg 1913, p. 264]:
   - *"There are equal numbers of black and white [atoms]"*
   - *"The arrangement of points black and white taken all together is that of the first cubic space lattice"* [simple cubic]
   - *"The arrangement of blacks alone or of whites alone is that of the third cubic space lattice"* [fcc]

5. **The lattice constant.** From Fig. 10 (p. 265), Bragg gives the nearest-neighbor distance in NaCl as **AB = 2.8 × 10⁻⁸ cm** (= 2.81 Å), corresponding to a cubic lattice parameter $a = 2 \times 2.81 = 5.62$ Å.

> **Historical note:** W. L. Bragg was 25 years old when he published this paper. He and his father W. H. Bragg were awarded the **1915 Nobel Prize in Physics** — W. L. Bragg remains the youngest Nobel laureate in physics.

#### Alkali Halide Lattice Parameters

| | F⁻ | Cl⁻ | Br⁻ |
|---|---|---|---|
| **Li⁺** | 4.027 | 5.130 | 5.501 |
| **Na⁺** | 4.620 | 5.640 | 5.977 |
| **K⁺** | 5.347 | 6.293 | 6.600 |
| **Rb⁺** | 5.630 | 6.581 | 6.889 |

*All values in Å, from X-ray diffraction.*

---

### 1.3.2 Cesium Chloride Structure

The cesium chloride structure (B2, space group $Pm\bar{3}m$) is *not* body-centered cubic, despite its visual appearance. It consists of two interpenetrating simple cubic lattices. Each Cs⁺ ion is surrounded by 8 Cl⁻ ions at the corners of a cube (coordination number 8), compared to 6 in the NaCl structure.

CsCl, CsBr, and CsI crystallize in this structure at atmospheric pressure, with lattice constants $a$ = 4.123 Å, 4.286 Å, and 4.567 Å respectively.

### 1.3.3 Hexagonal Close-Packed Structure

The hcp structure is not a Bravais lattice; it is a simple hexagonal lattice with a two-atom basis. For ideal close packing, the ratio $c/a = \sqrt{8/3} \approx 1.633$.

| Metal | $a$ (Å) | $c/a$ |
|-------|--------|-------|
| Be | 2.286 | 1.568 |
| Mg | 3.209 | 1.624 |
| Ti | 2.951 | 1.587 |
| Zn | 2.665 | 1.856 |
| Cd | 2.979 | 1.886 |
| Co | 2.507 | 1.623 |
| Zr | 3.232 | 1.593 |
| He (hcp, 0 K) | 3.570 | 1.633 |

The deviations from ideality are significant. Zinc and cadmium have $c/a$ ratios much larger than ideal, indicating weaker bonding between hexagonal layers. Only helium at 0 K and magnesium come close to the ideal ratio.

### 1.3.4 Diamond Structure

The diamond structure (A4, space group $Fd\bar{3}m$) is an fcc lattice with a two-atom basis: atoms at $(0,0,0)$ and $(1/4, 1/4, 1/4)$. Each atom is tetrahedrally bonded to four nearest neighbors.

Bond lengths $d = a\sqrt{3}/4$:
- C (diamond): $d$ = 1.545 Å
- Si: $d$ = 2.352 Å
- Ge: $d$ = 2.450 Å

### 1.3.5 Cubic Zinc Sulfide Structure

The zinc blende structure (B3, space group $F\bar{4}3m$) is identical to diamond but with two different atoms. III–V semiconductors (GaAs, InSb, GaP) and II–VI compounds (ZnS, CdTe) crystallize in this structure.

The key difference from diamond: zinc blende lacks inversion symmetry. This has consequences for piezoelectricity (Ch. 16) and nonlinear optics.

Bragg analyzed zincblende in his 1913 paper alongside the alkali halides. His Tables IV and V (p. 257) separate ZnS reflections into odd-index and even-index planes, establishing the fcc selection rule that would become fundamental to all of crystallography.

---

## 1.4 Direct Imaging of Atomic Structure

### 1.4.1 Transmission Electron Microscopy

The first direct images of a crystal lattice were obtained by J. W. Menter in 1956, who used transmission electron microscopy to image the lattice fringes of platinum phthalocyanine crystals with a spacing of 12 Å [Menter 1956]. This was a landmark — for the first time, the periodic arrangement of atoms in a crystal could be *seen* rather than merely inferred from diffraction patterns.

Modern aberration-corrected TEM can resolve individual atomic columns. Zhang et al. (2018) demonstrated atomic-resolution imaging of electron beam–sensitive crystalline materials using HRTEM, published in *Science* [Zhang 2018].

### 1.4.2 Scanning Tunneling Microscopy

The scanning tunneling microscope (STM), invented by Gerd Binnig and Heinrich Rohrer at IBM Zürich in 1981 (**Nobel Prize 1986**), provides real-space images of surfaces with atomic resolution. The STM measures the quantum mechanical tunneling current between a sharp metallic tip and the sample surface.

The iconic STM image of solid state physics is the Si(111)-7×7 surface reconstruction, which shows the arrangement of 49 atoms in the surface unit cell — a structure that could not have been determined by diffraction alone.

In 1990, Don Eigler and Erhard Schweizer at IBM Almaden positioned 35 xenon atoms on a nickel surface to spell "IBM" — the first demonstration of atomic-scale engineering [Eigler 1990]. We discuss this in detail in Chapter 18.

---

## 1.5 Crystal Structure Data

### Ionic Crystal Radii

R. D. Shannon compiled the most widely used set of effective ionic radii in 1976, based on a critical evaluation of over 1000 interatomic distances from X-ray and neutron diffraction studies.

| Ion | Radius (Å) | Ion | Radius (Å) |
|-----|-----------|-----|-----------|
| Li⁺ | 0.76 | F⁻ | 1.33 |
| Na⁺ | 1.02 | Cl⁻ | 1.81 |
| K⁺ | 1.38 | Br⁻ | 1.96 |
| Rb⁺ | 1.52 | I⁻ | 2.20 |
| Cs⁺ | 1.67 | O²⁻ | 1.40 |
| Mg²⁺ | 0.72 | S²⁻ | 1.84 |
| Ca²⁺ | 1.00 | Se²⁻ | 1.98 |
| Sr²⁺ | 1.18 | Te²⁻ | 2.21 |
| Ba²⁺ | 1.35 | | |

*Coordination number VI (octahedral). From Shannon (1976).*

### Radius Ratio Rules

The ratio $r_+/r_-$ governs which structure type is stable:

| Radius ratio | Structure | Coordination |
|-------------|-----------|-------------|
| $r_+/r_- > 0.732$ | CsCl | 8 |
| $0.414 < r_+/r_- < 0.732$ | NaCl | 6 |
| $0.225 < r_+/r_- < 0.414$ | Zinc blende | 4 |

For NaCl: $r_{\text{Na}^+}/r_{\text{Cl}^-} = 1.02/1.81 = 0.56$, which falls in the NaCl stability range. For CsCl: $r_{\text{Cs}^+}/r_{\text{Cl}^-} = 1.67/1.81 = 0.92$, correctly predicting the CsCl structure.

---

## References

1. **Bragg, W. L.** (1913). "The Structure of Some Crystals as Indicated by Their Diffraction of X-rays." *Proc. R. Soc. Lond. A* **89**, 248–277. DOI: [10.1098/rspa.1913.0083](https://doi.org/10.1098/rspa.1913.0083). — *The paper that founded X-ray crystallography. Contains the first determination of the NaCl structure, the fcc selection rule, and diffraction data for ZnS, KCl, KBr, KI, NaCl.*

2. **Menter, J. W.** (1956). "The Direct Study by Electron Microscopy of Crystal Lattices and Their Imperfections." *Proc. R. Soc. Lond. A* **236**, 119–135. DOI: [10.1098/rspa.1956.0117](https://doi.org/10.1098/rspa.1956.0117). — *First direct TEM images of crystal lattice fringes.*

3. **Zhang, D.** et al. (2018). "Atomic-Resolution Transmission Electron Microscopy of Electron Beam–Sensitive Crystalline Materials." *Science* **359**, 675–679. DOI: [10.1126/science.aao0865](https://doi.org/10.1126/science.aao0865).

4. **Eigler, D. M. and Schweizer, E. K.** (1990). "Positioning Single Atoms with a Scanning Tunnelling Microscope." *Nature* **344**, 524–526. DOI: [10.1038/344524a0](https://doi.org/10.1038/344524a0). — *35 Xe atoms positioned on Ni(110) to spell "IBM." 2708 citations.*

5. **Shannon, R. D.** (1976). "Revised Effective Ionic Radii and Systematic Studies of Interatomic Distances in Halides and Chalcogenides." *Acta Crystallogr. A* **32**, 751–767.
