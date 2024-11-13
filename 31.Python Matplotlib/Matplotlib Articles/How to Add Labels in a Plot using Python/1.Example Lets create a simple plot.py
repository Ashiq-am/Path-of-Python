# python program to plot graph without labels
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# it will take x coordinates by default
# starting from 0,1,2,3,4...
y = np.array([3, 8, 1, 10])

plt.plot(y)
plt.show()
