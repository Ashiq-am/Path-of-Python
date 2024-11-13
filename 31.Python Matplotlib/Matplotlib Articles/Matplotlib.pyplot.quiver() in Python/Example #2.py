# Python program to explain
# matplotlib.pyplot.quiver method

# importing necessary libraries
import matplotlib.pyplot as plt

# defining necessary arrays
x_coordinate = [0, 1.5]
y_coordinate = [0.5, 1.5]
x_direction = [1, -0.5]
y_direction = [1, -1]

# plotting the graph
plt.quiver(x_coordinate, y_coordinate,
		x_direction, y_direction,
		scale_units ='xy', scale = 1.)
