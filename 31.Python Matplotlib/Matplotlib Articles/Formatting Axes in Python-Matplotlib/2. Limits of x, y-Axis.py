import matplotlib.pyplot as plt
import numpy as np

x = [3, 2, 7, 4, 9]
y = [10, 4, 7, 1, 2]

# create a figure and axes
fig, ax = plt.subplots()

ax.set_title('Example Graph')

ax.set_ylabel('y-AXIS')
ax.set_xlabel('x-AXIS')

# set x, y-axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# function to plot and show graph
ax.plot(x, y)
plt.show()
