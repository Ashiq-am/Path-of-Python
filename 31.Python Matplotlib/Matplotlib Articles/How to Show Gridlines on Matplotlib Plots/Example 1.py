# Importing the library
import matplotlib.pyplot as plt

# Define X and Y data points
X = [12, 34, 23, 45, 67, 89]
Y = [1, 3, 67, 78, 7, 5]

# Plot the graph using matplotlib
plt.plot(X, Y)

# Add gridlines to the plot
plt.grid(b=True)
# `plt.grid()` also works

# Function to view the plot
plt.show()
