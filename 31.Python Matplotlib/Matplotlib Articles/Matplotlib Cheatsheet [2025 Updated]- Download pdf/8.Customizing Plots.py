# Sample data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create a customized plot
plt.plot(x, y, linestyle='-', color='purple', marker='o', markersize=8)

# Customize title and labels
plt.title("Customized Plot", fontsize=14, color='orange')
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)

# Display grid
plt.grid(True)

# Display the plot
plt.show()
