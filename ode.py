import numpy as np

def euler_1(model, y, t, dt):
    """ First-order Euler method """
    y1 = y + np.array(model(y, t)) * dt
    t1 = t + dt
    return y1, t1

def euler_2(model, y, t, dt):
    """ Second-order Euler method """
    k1 = np.array(model(y, t))
    k2 = np.array(model(y + k1 * dt, t))
    y1 = y + 0.5 * (k1 + k2) * dt
    t1 = t + dt
    return y1, t1

def ode_solve(model, initial_condition, integrator, dt, maxt):
    """ Numerical solution of a differential equation by the specified integrator.

        Arguments:
        model -- a function returning the right-hand side of the ODE
        dt -- step size
        maxt -- integration performed from t=0 to t=maxt

        Returns:
        list with solution [y0, y1, y2, ...]
        list with times [t0, t1, y2, ...]
    """
    y = np.array(initial_condition)         # Initial conditions
    ys = [y]
    
    t = 0
    ts = [t]
    
    while t < maxt:
        y, t = integrator(model, y, t, dt)
        
        ys.append(y)
        ts.append(t)
            
    return np.array(ys), np.array(ts)