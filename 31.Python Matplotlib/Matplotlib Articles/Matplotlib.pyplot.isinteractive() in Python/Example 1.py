# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y = np.sin(x ** 2) + np.cos(x)

plt.plot(x, y, label='Line 1')

plt.plot(x, y - 0.6, label='Line 2')

w = plt.isinteractive()

print("Is we can redraw after every plotting command : ",
      str(w))

plt.title('matplotlib.pyplot.isinteractive() function \
Example', fontweight="bold")

plt.show()
