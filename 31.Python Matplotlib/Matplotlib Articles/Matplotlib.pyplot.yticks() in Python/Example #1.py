# Implementation of matplotlib.pyplot.yticks()
# function

import numpy as np
import matplotlib.pyplot as plt

# values of x and y axes
valx = [30, 35, 50, 5, 10, 40, 45, 15, 20, 25]
valy = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]

plt.plot(valx, valy)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.xticks(np.arange(0, 60, 5))
plt.yticks(np.arange(0, 15, 1))
plt.show()
