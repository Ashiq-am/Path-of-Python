import numpy as np
import matplotlib.pyplot as plt

data = np.arange(100, 0, -1).reshape(10, 10)

fig, ax = plt.subplots()
cbaxes = fig.add_axes([0.28, 0.9, 0.49, 0.03])

im = ax.imshow(data, cmap='afmhot_r')

fig.colorbar(im, cax=cbaxes, orientation='horizontal')

plt.show()
