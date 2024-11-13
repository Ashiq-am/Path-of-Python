# Code to change the interval of ticks of axes
# using set_ticks() method

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating x-value and y-value of data
x = [1, 2, 3, 4]
y = [0.1, 0.2, 0.3, 0.4]

# Creating a sublpot with 2 row and 1 coloumn
fig, (axes1, axes2) = plt.subplots(2, 1)

# Plotting first axes object i.e. axes1 and labeling
# its x and y axes
axes1.plot(x, y)
axes1.set_ylabel('y-axis')
axes1.set_xlabel('x-axis')

# Setting the interval of ticks of x-axis to 1 and of y-axis
# to 0.1 of first axes i.e. axes1.
axes1.xaxis.set_ticks(np.arange(0, 5, 1))
axes1.yaxis.set_ticks(np.arange(0, 0.5, 0.1))

# Plotting first axes object i.e. axes1 and labeling its
# x and y axes
axes2.plot(x, y)
axes2.set_ylabel('y-axis')
axes2.set_xlabel('x-axis')

# Setting the interval of ticks of x-axis to 0.5 and
# of y-axis to 0.05 of second axes i.e. axes2.
axes2.xaxis.set_ticks(np.arange(0, 4.5, 0.5))
axes2.yaxis.set_ticks(np.arange(0, 0.45, 0.05))

# Giving title to the figure object i.e. fig
fig.suptitle('set_ticks() Example')
fig.tight_layout(pad=3.0)

plt.show()
