import matplotlib.pyplot as plt
import numpy as np

import ode

def ho(y, t):
    """ Derivatives for the harmonic osciilator """
    x, v = y
    return [v, -x]


ys1, ts1 = ode.ode_solve(ho, [0, 1], integrator=ode.euler_1, dt=0.1, maxt=10)

plt.plot(ts1, ys1[:,0], label="Euler 1")
plt.plot(ts1, np.sin(ts1), label="sin(t)")
plt.xlabel("t")
plt.ylabel("y")
plt.show()