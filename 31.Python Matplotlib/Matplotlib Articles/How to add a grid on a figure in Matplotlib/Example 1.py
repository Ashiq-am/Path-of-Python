import matplotlib.pyplot as plt
import numpy

# Define x and y
x = numpy.arange(0, 1, 0.1)
y = numpy.power(x, 2)

# Plot graph
plt.scatter(x, y)

# Define grid with axis='y'
plt.grid(axis='y')
plt.show()

# Define a figure
fig = plt.figure()
ax = fig.gca()

# Set labels on x and y axis of figure
ax.set_xticks(numpy.arange(0, 1, 0.1))
ax.set_yticks(numpy.arange(0, 1, 0.1))

# Plot the graph
ax.scatter(x, y)

# Specify default grid on figure
ax.grid()
ax.show()
