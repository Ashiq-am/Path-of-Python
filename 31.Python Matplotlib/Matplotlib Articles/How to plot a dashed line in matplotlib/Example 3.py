# Import libraries
import matplotlib.pyplot as plt

# Define Axes
X = [1.5, 5.6, 3.5, 4, 9]
Y1 = [1, 4, 3, 4, 5]
Y2 = [6, 7, 4, 9, 10]

# Plot a graph
plt.plot(X, Y1, linestyle='dashed', color='black')
plt.plot(X, Y2, linestyle='dashed',
		color='red', linewidth=4)

# Display graph
plt.show()
