import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Create a figure with a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot data in each subplot
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Plot 1')

axs[0, 1].scatter(x, y)
axs[0, 1].set_title('Plot 2')

axs[1, 0].pie(x, np.abs(y))
axs[1, 0].set_title('Plot 3')

axs[1, 1].hist(y, bins=30)
axs[1, 1].set_title('Plot 4')

fig.tight_layout()
plt.show()
