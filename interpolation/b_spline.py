
import numpy as np

def _open_uniform_knot_vector(n_ctrl, degree):
    m = n_ctrl + degree + 1
    kv = np.zeros(m, dtype=float)
    kv[degree:m-degree] = np.linspace(0, 1, m - 2*degree)
    kv[m-degree:] = 1.0
    return kv

def _de_boor(k, x, t, c, p):
    """De Boor algorithm to evaluate a clamped B-spline of degree p."""
    d = [c[j + k - p].astype(float).copy() for j in range(0, p+1)]
    for r in range(1, p+1):
        for j in range(p, r-1, -1):
            i = j + k - p
            denom = t[i+p+1-r] - t[i]
            alpha = 0.0 if denom == 0 else (x - t[i]) / denom
            d[j] = (1.0 - alpha) * d[j-1] + alpha * d[j]
    return d[p]

def b_spline_interpolate(waypoints, degree=3, num_samples=400):
    """Open-uniform (clamped) B-spline curve using waypoints as control points."""
    P = np.asarray(waypoints, dtype=float)
    n = P.shape[0]
    if n < 2:
        return P.copy()
    degree = min(degree, n-1)

    c = P.copy()
    t = _open_uniform_knot_vector(len(c), degree)

    u_start, u_end = t[degree], t[-degree-1]
    u = np.linspace(u_start, u_end, num_samples)

    path = np.zeros((num_samples, 2), dtype=float)
    for i, ui in enumerate(u):
        k = np.searchsorted(t, ui, side='right') - 1
        k = np.clip(k, degree, len(t) - degree - 2)
        path[i] = _de_boor(k, ui, t, c, degree)
    return path
