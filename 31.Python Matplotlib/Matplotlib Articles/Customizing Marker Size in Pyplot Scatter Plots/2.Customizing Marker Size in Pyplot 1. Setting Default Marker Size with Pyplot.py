import matplotlib.pyplot as plt
import matplotlib as mpl

# Set default marker size
mpl.rcParams['lines.markersize'] = 100

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

plt.scatter(x, y)
plt.show()
