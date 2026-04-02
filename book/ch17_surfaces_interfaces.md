# Chapter 17: Surface and Interface Physics

## Work Functions of Metals

The work function phi is the minimum energy to remove an electron from the metal surface to vacuum. Michaelson (1977) compiled a comprehensive review of recommended values.

> "A compilation of recommended values of work functions for polycrystalline and single crystal surfaces of the elements is presented." -- Michaelson, J. Appl. Phys. 48, 4729 (1977)

| Metal | phi (eV), polycrystalline | phi (eV), (111) face | Electron config.  |
|-------|--------------------------|---------------------|-------------------|
| Cs    | 2.14                     | 1.95                | [Xe]6s^1          |
| K     | 2.30                     | 2.30                | [Ar]4s^1          |
| Na    | 2.75                     | --                  | [Ne]3s^1          |
| Al    | 4.28                     | 4.24                | [Ne]3s^2 3p^1     |
| Cu    | 4.65                     | 4.94                | [Ar]3d^10 4s^1    |
| Au    | 5.10                     | 5.31                | [Xe]4f^14 5d^10 6s^1 |
| Pt    | 5.65                     | 5.93                | [Xe]4f^14 5d^9 6s^1  |
| W     | 4.55                     | 4.47                | [Xe]4f^14 5d^4 6s^2  |

Low work-function metals (Cs, K) are used as photocathodes; high work-function metals (Pt, Au) are preferred for Schottky barrier contacts.

## Surface Reconstruction: Si(111) 7x7

Clean semiconductor surfaces reconstruct to minimize dangling-bond energy. The Si(111)7x7 reconstruction, solved by Takayanagi et al. (1985) using transmission electron diffraction, contains 19 dangling bonds per unit cell (reduced from 49 in the unreconstructed surface). STM images by Binnig et al. (1983) provided the first real-space visualization.

## p-n Junction Current-Voltage Characteristics

The Shockley diode equation describes the ideal p-n junction:

I = I_0 [exp(eV / nkT) - 1]

| Parameter            | Si diode (typical) | Ge diode (typical) | GaAs diode   |
|---------------------|-------------------|-------------------|-------------|
| Saturation current I_0 | ~10^-12 A        | ~10^-7 A          | ~10^-18 A   |
| Ideality factor n    | 1.0-2.0           | 1.0-1.5            | 1.0-2.0     |
| Built-in voltage V_bi| 0.7 V             | 0.3 V              | 1.1 V       |
| Breakdown voltage    | 10-1000 V         | 5-200 V            | 5-100 V     |

## LED Emission Wavelengths

Light-emitting diodes exploit direct-gap semiconductor junctions. The emission wavelength is set by the band gap.

| Material system      | Band gap (eV) | Wavelength (nm) | Color         | Year demonstrated |
|---------------------|---------------|-----------------|---------------|-------------------|
| AlGaInP              | 1.9-2.3       | 540-650         | Green-Red     | 1990s             |
| GaAsP                | 1.8-2.1       | 590-690         | Yellow-Red    | 1962              |
| GaAs                 | 1.42          | 870             | Infrared      | 1962              |
| InGaN                | 2.0-3.4       | 365-520         | UV-Green      | 1993              |
| InGaN (blue)         | 2.64          | 470             | Blue          | 1993 (Nakamura)   |
| InGaN (white)        | --            | broadband       | White (phosphor) | 1996           |
| AlGaN                | 3.4-6.2       | 200-365         | Deep UV       | 2000s             |

Nakamura's development of efficient InGaN blue LEDs (Nobel Prize 2014) enabled white solid-state lighting.

## Integer Quantum Hall Effect

Von Klitzing, Dorda, and Pepper (1980) discovered the quantization of the Hall resistance in a Si MOSFET 2DEG at low temperature and high magnetic field.

> "The Hall voltage of a silicon MOS inversion layer shows well-defined plateaus... R_H = h/ie^2, where i is an integer." -- von Klitzing et al., PRL 45, 494 (1980)

| Plateau index i | R_H = h/(ie^2) (Ohm) | Measured accuracy        |
|----------------|----------------------|--------------------------|
| 1              | 25812.807            | parts per 10^9           |
| 2              | 12906.403            | parts per 10^9           |
| 3              | 8604.269             | parts per 10^9           |
| 4              | 6453.202             | parts per 10^10          |

The von Klitzing constant R_K = h/e^2 = 25812.80745... Ohm is now used as the resistance standard.

## Fractional Quantum Hall Effect

Tsui, Stormer, and Gossard (1982) discovered fractional quantization in high-mobility GaAs/AlGaAs heterostructures.

> "We observe a quantized Hall plateau... and a minimum in the diagonal resistivity... at filling factor nu = 1/3." -- Tsui et al., PRL 48, 1559 (1982)

| Fraction nu | R_H (h/e^2) | Discovery year | Explanation            |
|-------------|-------------|----------------|------------------------|
| 1/3         | 3 h/e^2     | 1982           | Laughlin wavefunction  |
| 2/3         | 3/2 h/e^2   | 1982           | Particle-hole of 1/3   |
| 2/5         | 5/2 h/e^2   | 1983           | Composite fermions     |
| 5/2         | 2/5 h/e^2   | 1987           | Non-Abelian (proposed) |

The FQHE states arise from strong electron-electron interactions forming an incompressible quantum liquid.

## References

1. H. B. Michaelson, "The work function of the elements and its periodicity," J. Appl. Phys. **48**, 4729 (1977). DOI: [10.1063/1.323539](https://doi.org/10.1063/1.323539)
2. K. von Klitzing, G. Dorda, and M. Pepper, "New Method for High-Accuracy Determination of the Fine-Structure Constant Based on Quantized Hall Resistance," Phys. Rev. Lett. **45**, 494 (1980). DOI: [10.1103/PhysRevLett.45.494](https://doi.org/10.1103/PhysRevLett.45.494)
3. D. C. Tsui, H. L. Stormer, and A. C. Gossard, "Two-Dimensional Magnetotransport in the Extreme Quantum Limit," Phys. Rev. Lett. **48**, 1559 (1982). DOI: [10.1103/PhysRevLett.48.1559](https://doi.org/10.1103/PhysRevLett.48.1559)
4. S. Nakamura et al., "High-brightness InGaN blue, green and yellow light-emitting diodes with quantum well structures," Jpn. J. Appl. Phys. **34**, L797 (1995). DOI: [10.1143/JJAP.34.L797](https://doi.org/10.1143/JJAP.34.L797)
5. G. Binnig et al., "7x7 Reconstruction on Si(111) Resolved in Real Space," Phys. Rev. Lett. **50**, 120 (1983). DOI: [10.1103/PhysRevLett.50.120](https://doi.org/10.1103/PhysRevLett.50.120)
