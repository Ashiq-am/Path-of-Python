# Setting x and y values for the plot
x = [1, 2, 3, 4]
y = [7, 13, 24, 22]

# Initiating the plot
plt.plot(x, y)
plt.title("PLOT")

# Setting the x and y labels
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

# Setting the number of ticks
plt.xlim(0, 3)
plt.locator_params(axis='x', nbins=3)

# Showing the plot
plt.show()
