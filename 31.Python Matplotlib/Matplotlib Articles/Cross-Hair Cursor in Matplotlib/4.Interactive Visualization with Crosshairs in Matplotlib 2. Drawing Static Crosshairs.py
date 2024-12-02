import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the scatter plot
np.random.seed(0)
x = np.random.rand(50) * 10  # 50 random values between 0 and 10 for the x-axis
y = np.random.rand(50) * 10  # 50 random values between 0 and 10 for the y-axis

# Create a figure and axis
fig, ax = plt.subplots()

# Scatter plot the data
ax.scatter(x, y, color='blue', label="Random Data Points")
ax.set_title("Scatter Plot with Static Crosshairs")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()

# Draw static crosshairs at the specified position (e.g., at x=5, y=5)
x_crosshair = 5  # X position for the vertical line
y_crosshair = 5  # Y position for the horizontal line

# Draw the horizontal and vertical lines (static crosshairs)
ax.axhline(y=y_crosshair, color='purple', linestyle='--', linewidth=2, label=f'Y={y_crosshair}')
ax.axvline(x=x_crosshair, color='purple', linestyle='--', linewidth=2, label=f'X={x_crosshair}')

# Add a label or text for clarity (static text near the crosshair)
ax.text(x_crosshair + 0.2, y_crosshair, f'({x_crosshair}, {y_crosshair})', color='purple')

# Display the plot
plt.show()