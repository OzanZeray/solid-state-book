# Chapter 18: Nanostructures

When the dimensions of a solid are reduced to the nanometer scale — comparable to the electron wavelength or the mean free path — quantum confinement and surface effects dominate. This chapter presents experimental data on imaging, manipulation, and electronic transport in one-dimensional (1D) and zero-dimensional (0D) systems.

---

## 18.1 Imaging Techniques for Nanostructures

### Scanning Tunneling Microscopy

The scanning tunneling microscope (STM), invented by Binnig and Rohrer in 1981 (Nobel Prize 1986), images surfaces by measuring the quantum mechanical tunneling current between a sharp metallic tip and the sample surface. The tunneling current depends exponentially on the tip-sample distance:

$$I \propto e^{-2\kappa d}, \quad \kappa = \sqrt{2m\phi}/\hbar$$

where $\phi$ is the work function (~4–5 eV for metals) and $d$ is the gap. A change of just 1 Å in $d$ changes the current by an order of magnitude — this is the basis for atomic resolution.

### Atomic Manipulation with the STM

**The landmark experiment: Eigler and Schweizer (1990).** Don Eigler and Erhard Schweizer at IBM Almaden used the STM at 4 K to position **35 individual xenon atoms** on a Ni(110) surface, spelling out "IBM." This was published in Nature (2708 citations) and remains one of the most iconic images in physics.

> *"Here we report the use of the STM at low temperatures (4 K) to position individual xenon atoms on a single-crystal nickel surface with atomic precision. This capacity has allowed us to fabricate rudimentary structures of our own design, atom by atom."* — Eigler and Schweizer, Nature 344, 524 (1990).

**The technique:** The STM tip is brought close enough to the Xe atom (~4 Å) that the van der Waals attraction between tip and atom exceeds the lateral diffusion barrier on the surface. The atom then follows the tip as it is moved laterally. At the desired position, the tip is retracted to release the atom.

**The atomic switch (1991).** Eigler, Lutz, and Rudge demonstrated that a single Xe atom could be transferred reversibly between the STM tip and the Ni surface by voltage pulses — the first single-atom switch. Published in Nature 352, 600 (1991) with **1132 citations**.

> *"We report the use of the STM to transfer a Xe atom back and forth between the tip of the microscope and a nickel surface."* — Eigler et al., Nature 352, 600 (1991).

**Quantum corrals (1993).** Crommie, Lutz, and Eigler arranged 48 iron atoms in a circular corral (radius ~71 Å) on Cu(111), directly imaging the standing wave pattern of surface-state electrons confined inside. This provided a stunning real-space visualization of quantum confinement.

### Modern Developments

Morgenstern, Lorente, and Rieder (2013) reviewed the evolution of atomic manipulation from individual atom positioning to scalable fabrication. Recent advances include:
- **Automated atomic assembly** using deep reinforcement learning (2022, 33 citations in Nature Communications)
- **Coherent spin manipulation** of individual atoms using pulsed STM (2019, Science, 161 citations)
- **Creating designer quantum states** atom-by-atom, including topological and magnetic phases (2019, Nature Reviews Physics, 142 citations)

---

## 18.2 Conductance Quantization

### Theory

In a quantum point contact — a narrow constriction between two electron reservoirs — the electrical conductance is quantized in units of the **conductance quantum**:

$$G_0 = \frac{2e^2}{h} = 7.748 \times 10^{-5} \text{ S} = (12\,906 \; \Omega)^{-1}$$

Each transverse mode that fits through the constriction contributes one quantum of conductance. As the constriction is widened (by gate voltage), the conductance increases in steps of $G_0$.

### Experimental Discovery

This was first observed independently by:
- **van Wees et al. (1988)** in a GaAs/AlGaAs quantum point contact defined by split gates
- **Wharam et al. (1988)** in a similar split-gate device

Both groups observed clean conductance staircases with plateaus at integer multiples of $G_0$, confirming the Landauer formula:

$$G = \frac{2e^2}{h} \sum_n T_n$$

where $T_n$ is the transmission probability of mode $n$.

### Conductance Quantization in Metallic Contacts

Gao et al. (2025) demonstrated conductance quantization in Cu quantum point contacts fabricated using STM atomic manipulation, showing that the quantization persists even in metallic systems with much shorter Fermi wavelengths.

---

## 18.3 Quantum Dots: Artificial Atoms

A quantum dot confines electrons in all three dimensions, producing discrete energy levels like an atom.

### Coulomb Blockade

When the charging energy $E_C = e^2/(2C)$ exceeds $k_B T$, adding a single electron to the dot requires a measurable voltage step $\Delta V = e/C$. As the gate voltage is swept, current flows only at discrete values — **Coulomb oscillations**.

### Characteristic Energy Scales

| Dot Type | Charging Energy $E_C$ (meV) | Level Spacing $\Delta E$ (meV) |
|----------|----------------------------|-------------------------------|
| GaAs lateral dot ($d \sim 100$ nm) | 1–5 | 0.1–0.5 |
| Self-assembled InAs dot | 20–50 | 10–30 |
| Metallic nanoparticle ($d \sim 5$ nm) | 50–200 | 0.01–0.1 |
| Single molecule (C₆₀) | 200–500 | 50–100 |

Allerbeck et al. (2025, Nature Communications) demonstrated **ultrafast Coulomb blockade** in an atomic-scale quantum dot, resolving charge transport through quantized defect states on femtosecond timescales.

### Semiconductor Nanocrystals (Quantum Dots)

Colloidal semiconductor nanocrystals (CdSe, InP, PbS) exhibit **size-tunable photoluminescence**: as the dot diameter decreases from ~6 nm to ~2 nm, the emission shifts from red to blue due to quantum confinement.

The confinement energy for a spherical dot of radius $R$:

$$E_n \approx E_g + \frac{\hbar^2 \pi^2 n^2}{2 m^* R^2}$$

This work, pioneered by Louis Brus and Moungi Bawendi, was recognized with the **2023 Nobel Prize in Chemistry**.

### The Kondo Effect in Quantum Dots

When a quantum dot has an odd number of electrons, it behaves like a magnetic impurity coupled to leads — a nanoscale realization of the Kondo effect (Ch. 22). Below the Kondo temperature $T_K$, the dot's spin is screened by the conduction electrons, and the conductance reaches the unitary limit $G = 2e^2/h$.

---

## 18.4 Vibrational and Thermal Properties of Nanostructures

### Quantized Vibrational Modes

In nanostructures, the phonon spectrum is modified by confinement. For a nanoparticle of diameter $d$, the lowest vibrational mode has frequency:

$$\nu \sim v_s / d$$

where $v_s$ is the sound velocity. For $d = 5$ nm and $v_s = 5000$ m/s: $\nu \sim 1$ THz.

### Heat Capacity

The heat capacity of nanostructures deviates from the bulk Debye $T^3$ law at low temperatures because the phonon spectrum has a minimum frequency cutoff set by the particle size.

---

## References

1. Eigler, D.M. and Schweizer, E.K. (1990). "Positioning single atoms with a scanning tunnelling microscope." **Nature 344, 524.** (2708 citations)
2. Eigler, D.M., Lutz, C.P., and Rudge, W.E. (1991). "An atomic switch realized with the scanning tunnelling microscope." Nature 352, 600. (1132 citations)
3. Crommie, M.F., Lutz, C.P., and Eigler, D.M. (1993). "Confinement of electrons to quantum corrals on a metal surface." Science 262, 218.
4. van Wees, B.J. et al. (1988). "Quantized conductance of point contacts in a two-dimensional electron gas." Phys. Rev. Lett. 60, 848.
5. Wharam, D.A. et al. (1988). "One-dimensional transport and the quantisation of the ballistic resistance." J. Phys. C 21, L209.
6. Morgenstern, K., Lorente, N., and Rieder, K.-H. (2013). "Controlled manipulation of single atoms and small molecules using the scanning tunnelling microscope." Phys. Status Solidi B 250, 1671.
7. Allerbeck, J. et al. (2025). "Ultrafast Coulomb blockade in an atomic-scale quantum dot." Nature Comm.
8. Yang, J. et al. (2019). "Coherent spin manipulation of individual atoms on a surface." Science 366, 509. (161 citations)
9. Khajetoorians, A.A. et al. (2019). "Creating designer quantum states of matter atom-by-atom." Nature Reviews Physics 1, 703. (142 citations)
