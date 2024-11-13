import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# set a random state for
# reproducibility
np.random.seed(19687581)

total_points = 500000
total_bins = 100

# Centering at a = 0 and b = 5
# generate normal distributions
a = np.random.randn(total_points)
b = .4 * a + np.random.randn(500000) + 5

figure, axes = plt.subplots(1, 2,
							tight_layout = True)

# C is the count in each bin
C, bins, patches = axes[0].hist(a,
								bins = total_bins)

# We'll color code by height,
# but you could use any scalar
fracs = C / C.max()

# Normalize of the data to 0..1
# for covering the full range of
# the colormap
norm = colors.Normalize(fracs.min(), fracs.max())

# looping through the objects and
# setting the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
	color = plt.cm.viridis(norm(thisfrac))
	thispatch.set_facecolor(color)

# normalize the inputs by C
axes[1].hist(a, bins = total_bins, density = True)

# formating the y-axis for displaying
# percentage
axes[1].yaxis.set_major_formatter(PercentFormatter(xmax = 1))
