import matplotlib.pyplot as plt
import numpy as np

import ode

def ho(y, t):
    """ Derivatives for the harmonic osciilator """
    x, v = y
    return [v, -x]


ys1, ts1 = ode.ode_solve(ho, [0, 1], integrator=ode.euler_1, dt=0.3, maxt=10)
ys2, ts2 = ode.ode_solve(ho, [0, 1], integrator=ode.euler_2, dt=0.3, maxt=10)
ys3, ts3 = ode.ode_solve(ho, [0, 1], integrator=ode.runge_kutta_4, dt=0.3, maxt=10)

plt.plot(ts1, ys1[:,0], label="Euler 1")
plt.plot(ts2, ys2[:,0], label="Euler 2")
plt.plot(ts3, ys3[:,0], label="Runge-Kutta 4")
plt.plot(ts1, np.sin(ts1), label="sin(t)")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()

print("Nakreslili jsme funkci sinus.")