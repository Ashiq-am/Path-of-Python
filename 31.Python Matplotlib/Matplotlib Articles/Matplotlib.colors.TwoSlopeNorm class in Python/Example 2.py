import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

data = np.random.normal(.4, 2, (10, 10))

two_slope_norm = mcolors.TwoSlopeNorm(vmin = data.min(),
									vmax = data.max(),
									vcenter = 0)

plt.imshow(data, cmap = plt.cm.RdBu,
		norm = two_slope_norm)

plt.colorbar()
plt.show()
