# Importing the libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# %matplotlib inline

# Setting x and y values for the plot
x = [1, 2, 3, 4]
y = [7, 13, 24, 22]

# Initiating the plot
plt.plot(x, y)
plt.title("PLOT")

# Setting the x and y labels
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

# Showing the plot
plt.show()
