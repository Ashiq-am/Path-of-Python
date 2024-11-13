# importing the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# creating the array to plot
x=np.arange(15)
y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 12,
15, 17, 19, 21, 23]

# making the scatter plot for x and y values
# giving color to the plot with respect to y
plt.scatter(x, y, c = y)

# naming the x axis and
# y axis using xlabel() and ylabel() function
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# visualizing the mapping from values to colors
plt.colorbar()

# giving title to the plot using plt.title() function
plt.title("Scatter Plot with Default colormap")

# visualizing the plot
plt.show()
