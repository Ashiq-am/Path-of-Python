# Code to add text on matplotlib

# Importing library
import matplotlib.pyplot as plt

# Creating x-value and y-value of data
x = [1, 2, 3, 4, 5]
y = [5, 8, 4, 7, 5]

# Creating figure
fig = plt.figure()

# Adding axes on the figure
ax = fig.add_subplot(111)

# Plotting data on the axes
ax.plot(x, y)

plt.show()
