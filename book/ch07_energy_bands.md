# Chapter 7: Energy Bands

The free electron model fails to explain why some materials are metals and others insulators. The resolution: solving the Schrödinger equation for electrons in the periodic potential of the crystal lattice produces energy bands separated by forbidden gaps.

---

## 7.1 Nearly Free Electron Model

A weak periodic potential $V(\mathbf{r})$ opens a **band gap** at each Brillouin zone boundary:

$$E_g = 2|V_\mathbf{G}|$$

States at the zone boundary form standing waves — one with density peaked on ions (lower energy), the other between ions (higher energy).

## 7.2 Bloch's Theorem

Felix Bloch (1928) proved that electron wavefunctions in a periodic potential have the form:

$$\psi_\mathbf{k}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_\mathbf{k}(\mathbf{r})$$

where $u_\mathbf{k}$ has the periodicity of the lattice.

## 7.3 Metals vs Insulators

- **Metal**: partially filled band — electrons at $E_F$ can be accelerated
- **Insulator**: filled bands separated by large gap ($E_g > 4$ eV)
- **Semiconductor**: small gap ($E_g \sim 0.1$–3 eV), allowing thermal excitation

## 7.4 Experimental Band Structure: ARPES

ARPES (angle-resolved photoemission spectroscopy) directly measures $E(\mathbf{k})$:

$$E_{binding} = h\nu - E_{kin} - \phi, \quad \hbar k_\parallel = \sqrt{2m E_{kin}} \sin\theta$$

Asonen et al. (1982) mapped the band structure of Cu alloy surfaces along (100), (110), (111), resolving the $d$-bands and $sp$-band [Asonen 1982].

## 7.5 Band Gap Temperature Dependence

Pässler (1999) compiled Varshni parameters for the empirical formula [Pässler 1999]:

$$E_g(T) = E_g(0) - \frac{\alpha T^2}{T + \beta}$$

| Material | $E_g(0)$ (eV) | Type | $\alpha$ (10⁻⁴ eV/K) | $\beta$ (K) | $E_g(300K)$ (eV) |
|----------|-------------|------|---------------------|-----------|----------------|
| Si | 1.170 | indirect | 4.73 | 636 | 1.12 |
| Ge | 0.744 | indirect | 4.77 | 235 | 0.66 |
| GaAs | 1.519 | direct | 5.41 | 204 | 1.42 |
| InP | 1.424 | direct | 4.50 | 327 | — |
| GaP | 2.338 | indirect | 6.20 | 460 | — |
| InSb | 0.235 | direct | 3.20 | 170 | 0.17 |

*From Pässler (1999), Phys. Status Solidi B 216, 975.*

## 7.6 Number of Orbitals in a Band

Each band holds $2N$ electrons (N primitive cells, 2 spins). Elements with an odd number of electrons per cell (Na, Cu, Al) are always metallic. Even-electron elements can be insulators if the gap is large enough (C, Si, Ge).

---

## References

1. **Pässler, R.** (1999). "Parameter Sets Due to Fittings of the Temperature Dependencies of Fundamental Bandgaps in Semiconductors." *Phys. Status Solidi B* **216**, 975. DOI: [10.1002/(SICI)1521-3951(199912)216:2<975::AID-PSSB975>3.0.CO;2-N](https://doi.org/10.1002/(SICI)1521-3951(199912)216:2<975::AID-PSSB975>3.0.CO;2-N).
2. **Asonen, H.** et al. (1982). "ARPES study of (100), (110), (111) surfaces of Cu₀.₉Al₀.₁." *Phys. Rev. B* **25**, 7075. DOI: [10.1103/PhysRevB.25.7075](https://doi.org/10.1103/PhysRevB.25.7075).
