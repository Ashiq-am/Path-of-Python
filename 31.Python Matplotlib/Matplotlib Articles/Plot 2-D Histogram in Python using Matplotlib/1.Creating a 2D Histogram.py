# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import random

# Creating dataset
from sympy.plotting.pygletplot import plot

n = 100
x = np.random.standard_normal(n)
y = 3.0 * x

fig = plt.subplots(figsize =(10, 7))
# Creating plot
plot.hist2d(x, y)
plot.title("Simple 2D Histogram")

# show plot
plot.show()
