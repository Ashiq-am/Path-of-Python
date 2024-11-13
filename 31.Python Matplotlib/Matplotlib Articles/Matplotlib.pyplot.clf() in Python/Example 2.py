# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)

plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.plot(t, s)
plt.grid(True)
plt.clf()

plt.title('matplotlib.pyplot.clf Example')
plt.show()
