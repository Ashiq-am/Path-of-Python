import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create some data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots()
sc = ax.scatter(x, y, c=y, cmap='viridis')

# Add a colorbar
colorbar = plt.colorbar(sc)

# Function to update the scatter plot and colorbar
def update(frame):
    y = np.sin(x + frame / 10.0)
    sc.set_array(y)
    colorbar.update_normal(sc)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.show()
