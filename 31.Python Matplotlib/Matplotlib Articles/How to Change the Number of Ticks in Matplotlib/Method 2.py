# Setting x and y values for the plot
x = [1, 2, 3, 4]
y = [7, 13, 24, 22]

# Initiating the plot
plt.plot(x, y, color='Red')
plt.title("PLOT")

# Setting the x and y labels
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

# Setting the number of ticks
plt.locator_params(axis='both', nbins=4)

# Showing the plot
plt.show()
