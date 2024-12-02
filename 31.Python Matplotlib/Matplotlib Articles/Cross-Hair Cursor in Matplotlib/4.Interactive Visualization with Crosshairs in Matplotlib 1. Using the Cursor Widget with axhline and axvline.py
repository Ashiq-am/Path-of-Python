import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor
matplotlib.use('TkAgg')  # Use TkAgg backend for GUI support


# Generate random data for the scatter plot
np.random.seed(0)
x = np.random.rand(50) * 10  # 50 random values between 0 and 10 for the x-axis
y = np.random.rand(50) * 10  # 50 random values between 0 and 10 for the y-axis

# Create a figure and axis
fig, ax = plt.subplots()

# Scatter plot the data
ax.scatter(x, y, color='blue', label="Random Data Points")
ax.set_title("Interactive Scatter Plot with Cross-Hair Cursor")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()

# Create the Cursor widget with blitting enabled
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)

# Show the plot
plt.show()