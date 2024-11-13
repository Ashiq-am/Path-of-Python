# importing the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# creating the array to plot
x=np.arange(15)
y=[1, 2, 3, 4, 5, 6, 7,
8, 9, 12, 15, 17, 19, 21, 23]

# getting the original colormap using cm.get_cmap() function
orig_map=plt.cm.get_cmap('viridis')

# reversing the original colormap using reversed() function
reversed_map = orig_map.reversed()

# making the scatter plot on x and y
# giving color to the plot with respect
# to y and passing cmap=reversed_map to reverse the colormap
plt.scatter(x, y, c = y, cmap = reversed_map)

# giving name to X and Y axis
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# visualizing the mapping from values to colors
plt.colorbar()

# giving title to the plot
plt.title("Scatter Plot with Default colormap")

# visualizing the plot using show() function
plt.show()
