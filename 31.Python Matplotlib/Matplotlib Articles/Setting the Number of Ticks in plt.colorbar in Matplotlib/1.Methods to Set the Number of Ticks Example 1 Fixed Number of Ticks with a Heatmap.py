import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(10, 10)
fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='coolwarm')
cbar = fig.colorbar(cax)
cbar.set_ticks([-3, -2, -1, 0, 1, 2, 3])
cbar.set_label('Value', rotation=270, labelpad=15)

plt.title('Heatmap with Fixed Number of Ticks')
plt.show()
