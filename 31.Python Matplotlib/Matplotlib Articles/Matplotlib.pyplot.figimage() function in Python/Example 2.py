import numpy as np
import matplotlib.pyplot as plt

im = np.zeros((40, 40, 3), dtype = np.float)

fig, ax = plt.subplots()
im = fig.figimage(im, 100, 60)

ax.scatter([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])

ax.set_zorder(1)
im.set_zorder(0)
ax.patch.set_visible(False)

plt.show()
