# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# dummy data
x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)

# creates two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 5))

# Plot without grid
ax1.plot(x1, y1)
ax1.set_title('Plot without grid')

# plot with grid
ax2.plot(x1, y1)
ax2.set_title("Plot with grid")

# draw gridlines
ax2.grid(True)

plt.show()
