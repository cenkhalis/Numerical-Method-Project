
import numpy as np

def _natural_cubic_spline_coeffs(t, y):
    """Compute natural cubic spline second derivatives (M) for y(t)."""
    n = len(t)
    if n < 3:
        return np.zeros(n, dtype=float)

    h = np.diff(t)
    A = np.zeros((n-2, n-2), dtype=float)
    d = np.zeros(n-2, dtype=float)

    for i in range(n-2):
        A[i, i] = 2 * (h[i] + h[i+1] if i+1 < len(h) else h[i] + h[i])

    for i in range(n-3):
        A[i, i+1] = h[i+1]
        A[i+1, i] = h[i+1]

    for i in range(1, n-1):
        d[i-1] = 6 * ((y[i+1]-y[i]) / h[i] - (y[i]-y[i-1]) / h[i-1])

    M_interior = np.linalg.solve(A, d)
    M = np.zeros(n, dtype=float)
    M[1:n-1] = M_interior
    return M

def _spline_eval(t, y, M, x):
    n = len(t)
    x = np.asarray(x, dtype=float)

    idx = np.searchsorted(t, x, side='right') - 1
    idx = np.clip(idx, 0, n-2)

    h = t[idx+1] - t[idx]
    a = (t[idx+1] - x) / h
    b = (x - t[idx]) / h
    return (a*y[idx] + b*y[idx+1] +
            ((a**3 - a)*M[idx] + (b**3 - b)*M[idx+1]) * (h**2)/6.0)

def cubic_spline_interpolate(waypoints, num_samples=400):
    """Natural cubic spline interpolation through waypoints in s=0..m-1."""
    waypoints = np.asarray(waypoints, dtype=float)
    m = waypoints.shape[0]
    if m < 2:
        return waypoints.copy()

    s = np.arange(m, dtype=float)
    Mx = _natural_cubic_spline_coeffs(s, waypoints[:, 0])
    My = _natural_cubic_spline_coeffs(s, waypoints[:, 1])

    u = np.linspace(0.0, m-1, num_samples)
    x = _spline_eval(s, waypoints[:, 0], Mx, u)
    y = _spline_eval(s, waypoints[:, 1], My, u)

    return np.column_stack([x, y])
