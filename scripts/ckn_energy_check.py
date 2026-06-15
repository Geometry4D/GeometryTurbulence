"""
Numerical verification of scaled energy quantities for CKN ε-regularity.

Computes the scale-invariant functionals A(r), C(r) over parabolic cylinders
for a test velocity field and tracks their behaviour as r → 0.

Usage:
    python ckn_energy_check.py
"""

import numpy as np
from scipy.integrate import dblquad


# ---------------------------------------------------------------------------
# Test velocity field: Burgers vortex (exact steady NS solution)
# Provides a non-trivial benchmark with known regularity.
# ---------------------------------------------------------------------------

def burgers_vortex(x, y, z, circulation=1.0, strain=1.0):
    """Velocity field of the Burgers vortex centred at the origin."""
    r2 = x**2 + y**2
    alpha = strain
    gamma = circulation
    # Azimuthal component (in Cartesian coordinates)
    factor = gamma / (2 * np.pi * r2 + 1e-12) * (1 - np.exp(-alpha * r2 / 2))
    u = -factor * y
    v =  factor * x
    w = -alpha * z
    return np.array([u, v, w])


# ---------------------------------------------------------------------------
# Scale-invariant energy functional A(r) at a point (x0, y0, z0, t0)
# A(r) = (1/r²) ∫∫_{Q_r} |u|³ dx dt   (simplified, pressure term omitted)
# ---------------------------------------------------------------------------

def scaled_energy_A(x0, y0, z0, r, n_sample=20):
    """
    Monte Carlo estimate of A(r) = (1/r²) * mean_{Q_r} |u|³ * vol(Q_r).
    Q_r = B_r(x0,y0,z0) × (t0 - r², t0)  — here t is a dummy parameter.
    """
    rng = np.random.default_rng(seed=42)
    # Sample points uniformly in the ball B_r × time interval
    pts = rng.uniform(-r, r, size=(n_sample**3, 3))
    inside = np.linalg.norm(pts, axis=1) < r
    pts = pts[inside] + np.array([x0, y0, z0])

    velocities = np.array([burgers_vortex(p[0], p[1], p[2]) for p in pts])
    u_cubed = np.linalg.norm(velocities, axis=1)**3

    vol_ball = (4/3) * np.pi * r**3
    time_interval = r**2
    vol_cylinder = vol_ball * time_interval

    integral = np.mean(u_cubed) * vol_cylinder
    return integral / r**2


# ---------------------------------------------------------------------------
# Main: compute A(r) for decreasing r
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("CKN scaled energy A(r) — Burgers vortex benchmark")
    print(f"{'r':>10}  {'A(r)':>14}  {'A(r)/r':>14}")
    print("-" * 42)

    radii = [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    x0, y0, z0 = 0.5, 0.0, 0.0  # evaluation point (off-axis)

    for r in radii:
        A = scaled_energy_A(x0, y0, z0, r)
        print(f"{r:>10.3f}  {A:>14.6f}  {A/r:>14.6f}")

    print()
    print("Note: for a regular point, A(r) → 0 as r → 0.")
    print("A positive limit would suggest a singularity candidate.")
