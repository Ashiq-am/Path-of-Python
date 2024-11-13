# Importing the necessary modules
import numpy as np
import matplotlib.pyplot as plt

# Creating a dataset
x = np.arange(0, 5, 0.1)
y = np.cos(x)

# Plotting the data
line1 = plt.plot(x, y)

# Legend
plt.figlegend((line1),('Cos'))
