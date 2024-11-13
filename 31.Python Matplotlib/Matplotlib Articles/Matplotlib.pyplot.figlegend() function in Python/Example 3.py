# Importing the necessary modules
import numpy as np
import matplotlib.pyplot as plt

# Creating a dataset
x = np.arange(0, 5, 0.1)
y = np.tan(x)

x1 = np.arange(0, 5, 0.1)
y1 = np.cos(x)

# Plotting the data
line1 = plt.plot(x, y)
line2 = plt.plot(x1, y1)

# Legend
plt.figlegend(
handles = (line1,line2),
		labels = ("Tan","Cos"),
		loc='upper right')
