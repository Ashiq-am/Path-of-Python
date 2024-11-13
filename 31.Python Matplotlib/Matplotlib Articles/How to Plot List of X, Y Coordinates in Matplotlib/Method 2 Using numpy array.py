# importing Matplotlib and Numpy Packages
import numpy as np
import matplotlib.pyplot as plt

# generating two arrays from 10 to 1 and from 1 to 10
x = np.arange(1, 11, 1)
y = np.arange(10, 0, -1)

# plot our list in X,Y coordinates
plt.scatter(x, y)
plt.show()
