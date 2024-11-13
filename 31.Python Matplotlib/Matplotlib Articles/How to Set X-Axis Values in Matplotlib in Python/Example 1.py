# Python program to set x-axis values in matplotlib

import matplotlib.pyplot as plt

# x-axis and y-axis values for ploting
x = [1, 2, 3, 4, 5, 6]
y = [3, 1, 4, 5, 3, 6]

# labels for x-asix
labels = ['A', 'B', 'C', 'D', 'E', 'F']

# Plotting x-axis and y-axis
plt.plot(x, y)

# naming of x-axis and y-axis
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

# naming the title of the plot
plt.title("Set X-Axis Values in Matplotlib")

# setting x-axis values
plt.xticks(x, labels)

plt.show()
