# importing packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

below = y < .5
above = y >= .5

# Plot lines below as dotted-------
plt.plot(x[below], y[below], '--')

# Plot lines above as solid_______
plt.plot(x[above], y[above], '-')

plt.show()
