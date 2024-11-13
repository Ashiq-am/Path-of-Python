# importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# creating the array to plot
x=np.arange(20)
y=[ 21, 24, 56, 78, 43, 23, 20, 28, 30,
4, 6, 5, 7, 89, 20, 12, 72, 51, 58, 18]

# making the scatter plot on x and y values and giving color w.r.t y
# passing cmap in cmap add _r at the end of colormap name to reverse the colormap
plt.scatter(x, y, c = y, cmap = 'viridis_r')

# giving name to X and Y axis
plt.xlabel("X")
plt.ylabel("Y")

# visualizing the mapping from values to colors
plt.colorbar()

# giving title to the plot
plt.title("Scatter Plot with Reveresed Viridis colormap")

# visualizing the plot using show() function
plt.show()
