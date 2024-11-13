# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import random

# Creating dataset
x = np.random.normal(size = 500000)
y = x * 3 + 4 * np.random.normal(size = 500000)

fig = plt.subplots(figsize =(10, 7))
# Creating plot
plt.plot.hist2d(x, y)
plt.plot.title("Simple 2D Histogram")

# show plot
plt.plot.show()
