import matplotlib.pyplot as plt
import numpy as np

array = np.arange(70, 0, -1).reshape(7, 10)
fig, ax = plt.subplots()

# This is the position for the colorbar
cbaxes = fig.add_axes([0.09, 0.12, 0.02, 0.7])

im = ax.imshow(array, cmap='afmhot_r')
plt.colorbar(im, cax=cbaxes)

# To show the plot
plt.show()
