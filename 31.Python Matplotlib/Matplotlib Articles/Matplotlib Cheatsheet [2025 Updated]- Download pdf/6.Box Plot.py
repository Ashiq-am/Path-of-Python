# Sample data
data = [np.random.normal(0, 1, 100) for _ in range(5)]

# Create a box plot
plt.boxplot(data)

# Add title and labels
plt.title("Box Plot")
plt.ylabel("Values")

# Display the plot
plt.show()
