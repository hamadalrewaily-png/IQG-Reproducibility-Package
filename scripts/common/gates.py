import numpy as np

def smooth_gate(u, eps):
    eps = float(eps)
    if eps <= 0:
        raise ValueError("eps must be > 0")
    return 0.5 * (1.0 + np.tanh(u / eps))

def heaviside_gate(u):
    return (u > 0).astype(float)

def gamma_from_gs(g_s, s_crit, eps_sbia=None, xi=None):
    g_s = np.asarray(g_s, dtype=float)
    if eps_sbia is None:
        gate = heaviside_gate(g_s - s_crit)
    else:
        gate = smooth_gate(g_s - s_crit, eps_sbia)
    if xi is None:
        return gate
    xi = np.asarray(xi, dtype=float)
    return gate * np.clip(xi, 0.0, None)
