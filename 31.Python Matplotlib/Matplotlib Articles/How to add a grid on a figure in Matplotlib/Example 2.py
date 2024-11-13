import matplotlib.pyplot as plt
import numpy as np

# Define x and y
x = np.arange(-5, 5, 0.01)
y = np.sin(2*np.pi*x)

# Plot line graph
plt.plot(x, y)

# Specify grid with line attributes
plt.grid(color='r', linestyle='--')

# Disply the plot
plt.show()
