
import numpy as np

def _barycentric_weights(t):
    n = len(t)
    w = np.ones(n, dtype=float)
    for j in range(n):
        diff = t[j] - np.delete(t, j)
        w[j] = 1.0 / np.prod(diff)
    return w

def _barycentric_eval(t, y, w, x):
    out = np.zeros_like(x, dtype=float)
    for i, xi in enumerate(x):
        diff = xi - t
        mask = np.isclose(diff, 0.0)
        if np.any(mask):
            out[i] = y[mask][0]
        else:
            out[i] = np.sum(w * y / diff) / np.sum(w / diff)
    return out

def lagrange_interpolate(waypoints, num_samples=300):
    """Global Lagrange interpolation (barycentric form) in s=0..m-1."""
    waypoints = np.asarray(waypoints, dtype=float)
    m = waypoints.shape[0]
    if m < 2:
        return waypoints.copy()

    s = np.arange(m, dtype=float)
    w = _barycentric_weights(s)

    u = np.linspace(0.0, m-1, num_samples)
    x = _barycentric_eval(s, waypoints[:, 0], w, u)
    y = _barycentric_eval(s, waypoints[:, 1], w, u)

    return np.column_stack([x, y])
