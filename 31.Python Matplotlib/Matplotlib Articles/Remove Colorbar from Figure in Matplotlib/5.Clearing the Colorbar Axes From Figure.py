import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(10, 10)
fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='viridis')

# Add a colorbar
colorbar = fig.colorbar(cax)
# Clear the colorbar axes
colorbar.ax.cla()
plt.show()
