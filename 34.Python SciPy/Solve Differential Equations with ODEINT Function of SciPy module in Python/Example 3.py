import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def returns_dydt(y,t):
	dydt = (1-y)/(1.95-y) - y/(0.05+y)
	return dydt

# initial conditions
y0 = [0, 1, 2]

# values of time
t = np.linspace(1,10)

# solving ODE
y = odeint(returns_dydt, y0, t)

# plot results
plt.plot(t,y)
plt.xlabel("Time")
plt.ylabel("Y")
plt.show()
