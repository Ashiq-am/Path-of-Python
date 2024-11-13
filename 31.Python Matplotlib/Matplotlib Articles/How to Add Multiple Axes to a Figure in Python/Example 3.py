# import matplotlib module
import matplotlib.pyplot as plt
# Creating an empty object
fig = plt.figure()

# Creation of multiple axes
# using add_axes
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])

# Creating the values
# of x and y for
# plotting graph
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Plotting axes1
axes1.plot(x, y)

# Plotting axes2
axes2.plot(x, y)

# Showing the figure
fig.show()
