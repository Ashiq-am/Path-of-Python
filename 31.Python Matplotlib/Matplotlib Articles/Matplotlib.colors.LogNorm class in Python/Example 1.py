import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Setting random state for
# reproducibility
np.random.seed(19680801)

max_points = 100000
all_bins = 20

# Generate a normal distribution,
# center at x = 0 and y = 5
a = np.random.randn(max_points)
b = .4 * a + np.random.randn(100000) + 5

figure, axes = plt.subplots(3, 1,
							figsize =(5, 15),
							sharex = True,
							sharey = True,
							tight_layout = True)

# Incrementing the number of
# bins on each axis
axes[0].hist2d(a, b, bins = 40)

# Defining normalization of
# the colors
axes[1].hist2d(a, b, bins = 40,
			norm = colors.LogNorm())

# defining custom numbers of bins
# for each axis
axes[2].hist2d(a, b, bins =(80, 10),
			norm = colors.LogNorm())

plt.show()
