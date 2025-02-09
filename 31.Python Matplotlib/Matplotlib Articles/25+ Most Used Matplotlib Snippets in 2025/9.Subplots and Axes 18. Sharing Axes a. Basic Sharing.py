import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a 2x1 grid of subplots sharing the x-axis
fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)

axs[0].plot(x, y1, color='blue')
axs[0].set_title('Sine Function')

axs[1].plot(x, y2, color='orange')
axs[1].set_title('Cosine Function')

# Adding labels
for ax in axs:
    ax.set_ylabel('Value')

plt.xlabel('X-axis (shared)')
plt.tight_layout()
plt.show()