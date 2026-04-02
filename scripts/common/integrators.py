import numpy as np

def euler_step(y, dt, rhs):
    return y + dt * rhs(y)

def rk4_step(y, dt, rhs):
    k1 = rhs(y)
    k2 = rhs(y + 0.5 * dt * k1)
    k3 = rhs(y + 0.5 * dt * k2)
    k4 = rhs(y + dt * k3)
    return y + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

def positivity_projection(arr):
    return np.maximum(arr, 0.0)
