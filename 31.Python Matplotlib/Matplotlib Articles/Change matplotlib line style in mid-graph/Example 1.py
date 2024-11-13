# importing packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.linspace(0, 10, 100)
y = 3 * x + 2

below = y < 15
above = y >= 15

# Plot lines below as dotted-------
plt.plot(x[below], y[below], '--')

# Plot lines above as solid________
plt.plot(x[above], y[above], '-')

plt.show()
