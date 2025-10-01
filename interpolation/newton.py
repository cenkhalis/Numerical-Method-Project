
import numpy as np

def _divided_differences(t, y):
    """Compute Newton divided differences coefficients."""
    n = len(t)
    coef = y.astype(float).copy()
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (t[j:n] - t[0:n-j])
    return coef

def _newton_eval(t, coef, x):
    """Evaluate Newton polynomial with base points t and coefficients coef at x."""
    n = len(coef)
    p = np.zeros_like(x, dtype=float)
    for k in range(n-1, -1, -1):
        p = coef[k] + (x - t[k]) * p
    return p

def newton_interpolate(waypoints, num_samples=300):
    """Interpolate waypoints with a global Newton polynomial in s=0..m-1."""
    waypoints = np.asarray(waypoints, dtype=float)
    m = waypoints.shape[0]
    if m < 2:
        return waypoints.copy()

    s = np.arange(m, dtype=float)
    sx = _divided_differences(s, waypoints[:, 0])
    sy = _divided_differences(s, waypoints[:, 1])

    u = np.linspace(0.0, m-1, num_samples)
    x = _newton_eval(s, sx, u)
    y = _newton_eval(s, sy, u)

    return np.column_stack([x, y])
