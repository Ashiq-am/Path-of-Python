# Import required module
import matplotlib.pyplot as plt
import numpy as np

# Assign axes
x = np.linspace(0,5.5,10)
y = 10*np.exp(-x)

# Assign errors regarding each axis
xerr = np.random.random_sample(10)
yerr = np.random.random_sample(10)

# Adjust plot
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='-o')

# Assign labels
ax.set_xlabel('x-axis'), ax.set_ylabel('y-axis')
ax.set_title('Line plot with error bars')

# Illustrate error bars
plt.show()
