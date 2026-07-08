# DNS Validation on a Real Navier–Stokes Field

**Program status: CLOSED (2026-06-22) — see [`../PROGRAM_CLOSEOUT.md`](../PROGRAM_CLOSEOUT.md). The measurements below are technically sound and retained; the closeout notes mark what they mean against the literature and the closed program lines.**

**Status: one solid positive result (orientation decorrelation confirmed on NS), one premise supported, structure functions unresolved at the available resolution.**

A pseudospectral DNS of forced isotropic turbulence (N = 128, single GPU, 4 GB) was run to test, on a genuine Navier–Stokes field rather than a Gaussian model, the predictions the program had only established for the model. This is the first externally-validated input to the program.

## Setup

Forced isotropic turbulence, N = 128, ν = 0.0035, 2/3 dealiasing, deterministic capped low-shell forcing, sampled over 15 steady-state snapshots. The resolution is modest (Re_λ low; no developed inertial range), which bounds what is and is not reliable below.

## Result 1 — orientation decorrelation, confirmed on NS

The expected value of $|\cos\angle(\xi_1^{(j)}, \xi_1^{(j+1)})|$ between dominant strain eigenvectors of adjacent octave bands:

| octave pair | E\|cos\| (DNS, NS field) |
|---|---|
| [4,8] – [8,16] | 0.436 ± 0.006 |
| [8,16] – [16,32] | 0.485 ± 0.001 |

Reference values: 0.500 for independent uniform directions on the sphere; ~0.49 for the Gaussian model studied earlier; 1.0 for perfect alignment.

The measured values (0.44–0.49) sit close to the independence reference and far from alignment. **On the real NS field the orientation of strain eigenvectors decorrelates across scales**, just as in the Gaussian model — the slight values below 0.5 indicate a mild anti-alignment that, if anything, reinforces decorrelation. This is the central outcome: the decorrelation result, previously established only for a Gaussian random field, now holds on genuine NS dynamics. It **partially closes the "model ≠ NS" barrier** for this specific result (the transversality input to Mode B). It does not address the analytic pressure-nonlocality barrier and says nothing about regularity.

> **Closeout note:** real and externally valid on NS — but **not novel**: cross-scale eigenframe orientation/alignment statistics are the established Ashurst (1987) / Elsinga–Marusic (2010) line. Retained as validation of the program's model prediction, not as a new measurement.

## Result 2 — premise (i) of Mode B, supported

Fraction of shear-like points (C_free, strain shape parameter |s| < 0.5) per octave:

| octave | φ_free |
|---|---|
| [4,8] | 0.50 |
| [8,16] | 0.56 |
| [16,32] | 1.0 — **artifact, discarded** |

On the resolved octaves φ_free ≈ 0.5, within the range expected from the literature on the strain shape-parameter PDF, and roughly scale-independent. This **supports premise (i)** (free zones present with positive fraction across inertial scales) as more than a postulate. The value 1.0 on [16,32] is a spectral-truncation artifact: that band is near the dealiasing cutoff where the field is essentially noise, so the shape test fires trivially; it is discarded.

> **Closeout note:** Mode B has since been closed as unrealizable at natural constants (see `../program/01_roadmap.md`); this premise support is retained as part of the historical record of that line.

## Result 3 — structure functions, unresolved at N = 128

Measured $\zeta_p \approx (1.9, 2.8, 3.8, 5.4)$ for $p = 2,3,4,6$, i.e. $\zeta_p \approx p$. Since the Kolmogorov 4/5 law fixes $\zeta_3 = 1$ exactly, $\zeta_3 = 2.8$ shows the separations sample the **dissipative range** ($\delta u(r) \sim r$, smooth), not an inertial range — at N = 128 there is no developed inertial interval. The anomaly $\zeta_6 - 2\zeta_3 = -0.29 \pm 0.23$ is negative in the mean (qualitatively consistent with intermittency) but the error bar spans both zero and the She–Lévêque value, so it is quantitatively uninformative. Calibration of the three-state model against structure-function exponents requires N > 256, beyond the available 4 GB. This is recorded honestly as a resolution limit, not a result.

## Net

The DNS delivered one solid, externally-validated positive result — orientation decorrelation on a real NS field — and turned premise (i) of Mode B from a postulate into a numerically supported statement. The structure-function calibration is out of reach at this resolution. The reliable findings are exactly those that do not require a wide inertial range; the rest is bounded by hardware, and is marked as such.
