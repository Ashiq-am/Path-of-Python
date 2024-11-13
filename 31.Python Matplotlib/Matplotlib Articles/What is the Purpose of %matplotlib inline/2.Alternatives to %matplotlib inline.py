# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Use the magic command
#%matplotlib inline

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X values")
plt.ylabel("Sine of X")
plt.show()
