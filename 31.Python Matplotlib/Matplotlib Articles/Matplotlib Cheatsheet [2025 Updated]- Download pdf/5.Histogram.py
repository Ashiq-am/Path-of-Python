import numpy as np

# Generate random data
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=30, color='blue', edgecolor='black')

# Add title and labels
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Display the plot
plt.show()
