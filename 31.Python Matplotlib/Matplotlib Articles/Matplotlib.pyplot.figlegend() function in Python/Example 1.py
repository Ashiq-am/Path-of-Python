# Importing the necessary modules
import numpy as np
import matplotlib.pyplot as plt

# Creating a dataset
x = np.arange(0, 5, 0.1)
y = np.sin(x)

# Plotting the data
plt.plot(x, y, label = "Sin")

# Legend
plt.figlegend()
