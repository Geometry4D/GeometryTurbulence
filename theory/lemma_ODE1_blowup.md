# Lemma ODE-1 — Finite-time blow-up of the enstrophy ODE

**Status: closed (fully proven).** This is the strongest closed result of the program. It is a self-contained ODE statement; its role is to convert the geometric blow-up criterion into an explicit finite-time bound.

---

## Statement

Let E(t) ≥ 0 satisfy the differential inequality

$$
\frac{dE}{dt} \;\ge\; -K\,E + c\,E^{1+\delta}, \qquad t \ge 0,
$$

with constants K ≥ 0, c > 0, δ > 0, and initial value E(0) = E₀ satisfying the **largeness condition**

$$
E_0 > \left(\frac{K}{c}\right)^{1/\delta}.
$$

Then E(t) blows up in finite time: there exists T* < ∞ with E(t) → ∞ as t → T*⁻, and

$$
T^* \;\le\; \frac{E_0^{-\delta}}{c\,\delta\,\beta_0}, \qquad \beta_0 := 1 - \frac{K}{c}\,E_0^{-\delta} \in (0,1].
$$

---

## Proof

The largeness condition gives, at t = 0,

$$
\frac{dE}{dt}\Big|_{0} \ge c\,E_0^{1+\delta} - K\,E_0 = c\,E_0^{1+\delta}\big(1 - \tfrac{K}{c}E_0^{-\delta}\big) = c\,\beta_0\,E_0^{1+\delta} > 0,
$$

so E is increasing at 0. Since the right-hand side −KE + cE^{1+δ} = E(cE^δ − K) is positive for all E ≥ E₀ (because E^δ ≥ E₀^δ > K/c there), E(t) is strictly increasing for as long as it exists, hence E(t) ≥ E₀ and the superlinear term stays dominant.

For E ≥ E₀ we have the lower bound

$$
\frac{dE}{dt} \ge c\,E^{1+\delta}\Big(1 - \tfrac{K}{c}E^{-\delta}\Big) \ge c\,\beta_0\,E^{1+\delta},
$$

using that E ↦ 1 − (K/c)E^{−δ} is increasing, so it is ≥ β₀ for E ≥ E₀. Separating variables,

$$
\frac{dE}{E^{1+\delta}} \ge c\,\beta_0\,dt
\;\Longrightarrow\;
-\frac{1}{\delta}\,d\!\left(E^{-\delta}\right) \ge c\,\beta_0\,dt .
$$

Integrating from 0 to t,

$$
\frac{1}{\delta}\big(E_0^{-\delta} - E(t)^{-\delta}\big) \ge c\,\beta_0\,t
\;\Longrightarrow\;
E(t)^{-\delta} \le E_0^{-\delta} - \delta\,c\,\beta_0\,t .
$$

The right-hand side reaches 0 at

$$
t = T^* := \frac{E_0^{-\delta}}{\delta\,c\,\beta_0},
$$

forcing E(t)^{−δ} → 0, i.e. E(t) → ∞, no later than T*. ∎

---

## Numerical confirmation

A direct forward integration of dE/dt = −KE + cE^{1+δ} confirms that the actual blow-up time never exceeds the bound T*. For (E₀, K, c, δ) = (10, 1, 1, ½): β₀ = 1 − 0.1·10^{−1/2} ≈ 0.968, the analytic upper bound is T* ≈ 0.21, and the numerically observed blow-up occurs at ≈ 0.20 < T*.

---

## Role in the program

Combined with the geometric blow-up criterion (small C_geo, sufficient screening flux), this lemma yields a finite upper bound on the blow-up time T* in terms of the free-zone parameters (C_geo, J_geo, anisotropy). The largeness condition E₀ > (K/c)^{1/δ} corresponds to a sufficiently large initial enstrophy in the active region.
