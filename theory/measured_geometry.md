# Measured Geometry of Strain Classes in Navier–Stokes

**Status: a coherent, DNS-measured structural picture. One solid bridge (energy flux), a robust transition structure, one honestly negative result (intermittency is not a class effect at the accessible resolution).**

This collects what local DNS (N = 128, single GPU) measured directly about the strain-class geometry, both Eulerian (per-class diagnostics over a stationary window) and Lagrangian (class dynamics along tracer trajectories). Everything here passed a two-sided check; the negative result is recorded with equal weight.

---

## 1. Energy flux per class — free zones are zero-flux zones (solid)

The energy-flux density $\Pi = -\mathrm{tr}(e^3) - \tfrac14\,\omega\cdot e\cdot\omega$ (Eyink; Borue–Orszag), averaged per class on the NS field:

| class | mean flux $\Pi$ | role |
|---|---|---|
| C_small | $-1.7\times10^{-5}$ | sink (forward cascade) |
| C_free | $-4.7\times10^{-7}$ | **buffer (≈ zero)** |
| C_large | $+7.3\times10^{-6}$ | source |

C_free carries flux about **36× smaller** in magnitude than C_small. The signs are structural — C_small a sink, C_large a source, C_free a near-zero buffer — and are stable between the N = 16 sanity run and the full N = 128 run (only the absolute magnitudes drift as the field weakens). This **measures**, on a real NS field, the previously analytic claim that free zones are zones of suppressed energy flux. It restates the known flux decomposition in the language of the strain classes; it is a bridge, not a new result about anomalous dissipation itself.

## 2. Lagrangian class dynamics — persistence hierarchy and transition structure (robust)

Tracking ~$10^4$–$2\times10^4$ passive tracers along trajectories and recording the strain class at each particle:

- **Persistence hierarchy (robust):** C_free is the longest-lived class, C_small the shortest-lived and rarest (occupancy ≈ 4 %). This ordering is stable across very different integration horizons, even as absolute lifetimes drift with the (non-stationary) field. Free zones are the persistent skeleton of the flow; strong stretching is a rare, short-lived event.
- **Transition structure (robust):** direct C_small ↔ C_free transitions are essentially absent; transitions between them pass through C_large. Stable across all runs.
- **Quantitative parameters are NOT reliable:** per-class drift, noise, and absolute lifetimes drift monotonically over long runs because the forced field slowly relaxes (the capped forcing does not hold a true steady state over $10^5$ steps). Only the *ordering* and *connectivity* are robust; the numbers are not. Methodological lesson: use short stationary windows or ensembles, not single long runs.

## 3. Intermittency is not a class effect at this resolution (negative)

Flatness of $|\nabla u|$ per class (Gaussian = 3):

| | C_small | C_free | C_large | full |
|---|---|---|---|---|
| flatness | 2.70 | 3.30 | 3.22 | 3.27 |

The full-field flatness (3.27) is only marginally super-Gaussian, and **C_small — the strong-stretching class — is sub-Gaussian (2.70), i.e. the most regular class, not the bursty one** (a single dominant stretching direction gives a structured gradient). An apparent signal in the N = 16 sanity run (C_small flatness 3.95) did **not** survive at N = 128 and is attributed to negligible statistics there. Conclusion: at the accessible Reynolds number there is no class-resolved intermittency picture, and C_small is not its carrier. Developed intermittency would require N > 256, beyond the available 4 GB. This, together with the earlier finding that the three-state model reproduces intermittency only under parameter heterogeneity not present in the measured flow, **closes the intermittency line** within the current means.

## 4. Vorticity–strain alignment — not developed (neutral)

$|\cos\angle(\omega,e_i)|$ per class is ≈ 0.5 for all axes and all classes; the Ashurst intermediate-axis alignment ($\omega \to e_2$) is not visible at this resolution. Neutral, resolution-limited.

## 5. Scale dependence (supporting)

Per-octave class fractions are stable across the two resolved octaves (C_small ≈ 4 %, C_free ≈ 50 %, C_large ≈ 46 %); the smallest octave is a spectral-truncation artifact and is discarded. This supports premise (i) of the conditional dimension result (free zones present with a positive, roughly scale-independent fraction).

---

## The coherent picture

The reliable measurements assemble into one internally consistent structural statement about Navier–Stokes turbulence at this resolution:

> Free zones (C_free) form a persistent, volume-dominant (~50 %) skeleton of the flow that carries almost no energy flux; strong stretching (C_small) occupies rare (~4 %), short-lived sink regions; transitions between the two are routed through an intermediate class; and eigenvector orientation decorrelates across scales (E\|cos\| ≈ 0.44–0.49, separate DNS).

This is a measured geometric description, not a theorem about regularity and not a mechanism for intermittency — both of those lines are closed. Its value is a coherent, externally-validated structural account of where energy flux lives, which geometric regions persist, and how they connect. Confidence is high for the flux ordering, the persistence hierarchy, and the transition structure; the negative intermittency result is firm at this resolution; absolute Lagrangian parameters are not claimed.
