# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots()

axs.plot(np.random.random((10, 10)))

plt.subplot_tool()

fig.suptitle('matplotlib.pyplot.subplot_tool() Example')
plt.show()
