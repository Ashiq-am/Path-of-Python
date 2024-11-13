# Importing library
import matplotlib

# Create figure() objects
# This acts as a container
# for the different plots
fig = matplotlib.pyplot.figure()

# Creating two axes
# add_axes([xmin,ymin,dx,dy])
axes = fig.add_axes([0,0,2,2])
axes1 = fig.add_axes([0,1,2,2])

# Depict illustration
fig.show()
