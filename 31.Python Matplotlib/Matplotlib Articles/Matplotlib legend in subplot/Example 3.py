# importing modules
from matplotlib import pyplot

# assign value to x axis
x_axis = list(range(-10, 10))

# get the value of x*x
y_axis1 = [x*x for x in x_axis]

# get the value of x*x*x
y_axix2 = [x*x*x for x in x_axis]

# create subplots using subplot() method
fig, axes = pyplot.subplots(2)

# depicting the visualization
axes[0].scatter(x_axis, y_axis1, color='green', marker='*', label="y=x^2")
axes[1].scatter(x_axis, y_axix2, color='red', marker='*', label="y=x^3")

# position at which legend to be added
axes[0].legend(loc='best')
axes[1].legend(loc='best')

# display the plot
pyplot.show()
