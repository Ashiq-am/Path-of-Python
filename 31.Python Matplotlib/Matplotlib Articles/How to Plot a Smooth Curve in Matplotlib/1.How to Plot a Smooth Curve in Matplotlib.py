import numpy as np
import matplotlib.pyplot as plt

# Dataset
x = np.array([ 1, 2, 3, 4, 5, 6, 7, 8 ])
y = np.array([ 20, 30, 5, 12, 39, 48, 50, 3 ])

# Plotting the Graph
plt.plot(x, y)
plt.title("Curve plotted using the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
