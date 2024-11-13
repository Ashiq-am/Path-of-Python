import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from numpy.random import multivariate_normal

# data for reproducibality
data = np.vstack([
    multivariate_normal([10, 10],
                        [[3, 2],
                         [2, 3]],
                        size=100000),

    multivariate_normal([30, 20],
                        [[2, 3],
                         [1, 3]],
                        size=1000)
])

gammas_array = [0.9, 0.6, 0.4]

figure, axs = plt.subplots(nrows=2,
                           ncols=2)

axs[0, 0].set_title('Linear normalization')
axs[0, 0].hist2d(data[:, 0],
                 data[:, 1],
                 bins=100)

for ax, gamma in zip(axs.flat[1:],
                     gammas_array):
    ax.set_title(r'Power law $(\gamma =% 1.1f)$' % gamma)
    ax.hist2d(data[:, 0],
              data[:, 1],
              bins=100,
              norm=mcolors.PowerNorm(gamma))

figure.tight_layout()

plt.show()
