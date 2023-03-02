import matplotlib.pyplot as plt
import ode

def relaxation(y, t):
    """ Derivatives for the relaxing system """
    return -y

ys, ts = ode.ode_solve(relaxation, 1, integrator=ode.euler_1, dt=0.01, maxt=10)

plt.plot(ts, ys)
plt.xlabel("t")
plt.ylabel("y")
plt.show()