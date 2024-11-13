# importing libraries
import matplotlib.pyplot as plt
import numpy as np

# creating two array for plotting
x = np.arange(-20, 20, 1)
y = [-30, -20, -10, -3, 1, 11, 10, 5, -20, 20, 15, 30, 20,
	2, 4, 3, -7, -8, -13, -16, 16, -15, 32, -12, -19, 25,
	-25, 30, -6, -18, -11, -14, -21, 27, -21, -14, -4, -1, 0, 17]

# creating scatter plot with both negative
# and positive axes
plt.scatter(x, y)

# adding vertical line in data co-ordinates
plt.axvline(0, c='black', ls='--')

# adding horizontal line in data co-ordinates
plt.axhline(0, c='black', ls='--')

# visualizing the plot using plt.show() function
plt.show()
