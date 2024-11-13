# python program for plots with label
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# Number of chidern it was default in earlier case
x = np.array([0, 1, 2, 3])

# Number of families
y = np.array([3, 8, 1, 10])

plt.plot(x, y)

# Label for x-axis
plt.xlabel("Number of Childerns")

# Label for y-axis
plt.ylabel("Number of Families")

plt.show() # for display
