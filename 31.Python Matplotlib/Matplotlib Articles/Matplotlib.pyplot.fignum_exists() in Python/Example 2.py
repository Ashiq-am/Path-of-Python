# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y = np.sin(x ** 2) + np.cos(x)

plt.plot(x, y, label='Line 1')
plt.plot(x, y - 0.6, label='Line 2')

plt.text(2.5, 1.9,
         "Figure 2 Exists ? " +
         str(plt.fignum_exists(2)),
         fontweight="bold")

plt.title('matplotlib.pyplot.fignum_exists()function\
Example', fontweight="bold")

plt.show()
