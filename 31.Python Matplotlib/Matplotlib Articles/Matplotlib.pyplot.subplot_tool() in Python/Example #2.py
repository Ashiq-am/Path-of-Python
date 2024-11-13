# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, (axs, axs1) = plt.subplots(1, 2)

axs.pcolor(np.random.random((10, 10)))
axs1.imshow(np.random.random((10, 10)))

plt.subplot_tool()

fig.suptitle('matplotlib.pyplot.subplot_tool() Example')
plt.show()
