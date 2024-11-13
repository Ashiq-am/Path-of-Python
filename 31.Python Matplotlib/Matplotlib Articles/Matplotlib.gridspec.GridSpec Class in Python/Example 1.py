import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


gs = GridSpec(8, 39)
ax1 = plt.subplot(gs[:6, :35])
ax2 = plt.subplot(gs[6:, :])

data1 = np.random.rand(6, 35)
data2 = np.random.rand(2, 39)

ax1.imshow(data1)
ax2.imshow(data2)

plt.show()
