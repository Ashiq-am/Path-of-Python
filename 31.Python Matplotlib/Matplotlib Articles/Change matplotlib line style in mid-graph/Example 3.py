# importing packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

below = abs(y1-y2) < .2
above = abs(y1-y2) >= .2

# Plot lines below as dotted-------
plt.plot(x[below], y1[below], 'r--')

# Plot lines below as dotted-------
plt.plot(x[below], y2[below], 'g--')

# Plot lines above as solid_______
plt.plot(x[above], y1[above], 'r-')

# Plot lines above as solid_______
plt.plot(x[above], y2[above], 'g-')

plt.show()
