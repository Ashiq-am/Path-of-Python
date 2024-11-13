import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import from_levels_and_colors

nvals = np.random.randint(2, 20)
data = np.random.randint(0, nvals,
						(10, 10))

colors = np.random.random((nvals, 3))
# Make the colors pastels...
colors = colors / 2.5 + 0.55

levels = np.arange(nvals + 1) - 0.5
cmap, norm = from_levels_and_colors(levels,
									colors)

fig, ax = plt.subplots()
im = ax.imshow(data,
			interpolation ='nearest',
			cmap = cmap,
			norm = norm)

fig.colorbar(im, ticks = np.arange(nvals))
plt.show()
