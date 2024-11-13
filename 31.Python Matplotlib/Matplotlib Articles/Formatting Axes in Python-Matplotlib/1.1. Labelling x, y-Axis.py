# importing matplotlib module
import matplotlib.pyplot as plt
import numpy as np

# x-axis & y-axis values
x = [3, 2, 7, 4, 9]
y = [10, 4, 7, 1, 2]

# create a figure and axes
fig, ax = plt.subplots()

# setting title to graph
ax.set_title('Example Graph')

# label x-axis and y-axis
ax.set_ylabel('y-AXIS')
ax.set_xlabel('x-AXIS')

# function to plot and show graph
ax.plot(x, y)
plt.show()
