import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(100, 100)

fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='plasma')
cbar = fig.colorbar(cax)

ticks = np.linspace(data.min(), data.max(), num=7)
cbar.set_ticks(ticks)

cbar.set_label('Random Value', rotation=270, labelpad=15)

plt.title('Image Plot with Regular Interval Ticks')
plt.show()
