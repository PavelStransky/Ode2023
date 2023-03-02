import matplotlib.pyplot as plt

def euler_1(model, y, t, dt):
    y1 = y + model(y, t) * dt
    t1 = t + dt
    return y1, t1

def ode_solve(model, initial_condition, integrator, dt, maxt):
    y = initial_condition
    ys = [y]
    
    t = 0
    ts = [t]
    
    while t < maxt:
        y, t = integrator(model, y, t, dt)
        
        ys.append(y)
        ts.append(t)
            
    return ys, ts

def relaxation(y, t):
    return -y

ys, ts = ode_solve(relaxation, 1, integrator=euler_1, dt=0.01, maxt=10)

plt.plot(ts, ys)
plt.xlabel("t")
plt.ylabel("y")
plt.show()