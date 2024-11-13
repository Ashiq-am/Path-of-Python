# Importing library
import matplotlib

# Create figure() objects
# This acts as a container
# for the different plots
fig = matplotlib.pyplot.figure()

# Creating axis
# add_axes([xmin,ymin,dx,dy])
axes = fig.add_axes([0.5, 1, 0.5, 1])

# Depict illustration
fig.show()
