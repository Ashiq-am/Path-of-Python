import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

# Creating Multiple Subplots for Line Plots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Line Plot 1
axes[0, 0].plot(x, y1, label='sin(x)', color='blue')
axes[0, 0].set_title('Line Plot 1')
axes[0, 0].legend()

# Line Plot 2
axes[0, 1].plot(x, y2, label='cos(x)', color='orange')
axes[0, 1].set_title('Line Plot 2')
axes[0, 1].legend()

# Line Plot 3
axes[1, 0].plot(x, y3, label='tan(x)', color='green')
axes[1, 0].set_title('Line Plot 3')
axes[1, 0].legend()

# Line Plot 4
axes[1, 1].plot(x, y4, label='exp(-x)', color='red')
axes[1, 1].set_title('Line Plot 4')
axes[1, 1].legend()

# Adjusting layout
plt.tight_layout()

# Show the plots
plt.show()
