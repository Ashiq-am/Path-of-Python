import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Make some illustrative fake data:
a = np.arange(0, np.pi, 0.1)
b = np.arange(0, 2 * np.pi, 0.1)
A, B = np.meshgrid(a, b)
X = np.cos(A) * np.sin(B) * 10

# colormap froma list
# R -> G -> B
list_colors = [(1, 0, 0),
               (0, 1, 0),
               (0, 0, 1)]

# Discretizes the interpolation
# into bins
all_bins = [3, 6, 10, 100]
cmap_name = 'my_list'
figure, axes = plt.subplots(2, 2,
                            figsize=(6, 9))

figure.subplots_adjust(left=0.02,
                       bottom=0.06,
                       right=0.95,
                       top=0.94,
                       wspace=0.05)

for all_bin, ax in zip(all_bins, axes.ravel()):
    # Making the the colormap
    cm = LinearSegmentedColormap.from_list(
        cmap_name,
        list_colors,
        N=all_bin)

    im = ax.imshow(X, interpolation='nearest',
                   origin='lower', cmap=cm)

    ax.set_title("bin: % s" % all_bin)
    fig.colorbar(im, ax=ax)
