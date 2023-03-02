def euler_1(model, y, t, dt):
    """ First-order Euler method """
    y1 = y + model(y, t) * dt
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
    y = initial_condition
    ys = [y]
    
    t = 0
    ts = [t]
    
    while t < maxt:
        y, t = integrator(model, y, t, dt)
        
        ys.append(y)
        ts.append(t)
            
    return ys, ts