def f(t, x):
    return -x

def runge_kutta_4th_order(t, x, dt):
    k1 = dt * f(t, x)
    k2 = dt * f(t + 0.5*dt, x + 0.5*k1)
    k3 = dt * f(t + 0.5*dt, x + 0.5*k2)
    k4 = dt * f(t + dt, x + k3)
    return x + (k1 + 2*k2 + 2*k3 + k4) / 6

# Initial conditions
t0 = 0
x0 = 1

# Time step and number of iterations
dt = 10**(-1)
iterations = int(10 / dt)

# Perform the iterations
t = t0
x = x0
for _ in range(iterations):
    x = runge_kutta_4th_order(t, x, dt)
    t += dt

# Print the result
print("{:.15f}".format(x))
