# Sample data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create plot
plt.plot(x, y)

# Add grid
plt.grid(True, which='both', axis='both', linestyle=':', color='gray')

# Customize axes limits
plt.xlim(0, 5)
plt.ylim(0, 30)

# Add title and labels
plt.title("Plot with Grid and Customized Axes")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot
plt.show()
