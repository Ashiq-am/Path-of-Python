# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec


fig = plt.figure(tight_layout = True)
gs = gridspec.GridSpec(1, 1)

ax = fig.add_subplot(gs[0, :])
ax.plot(np.arange(0, 1e6, 1000))
ax.set_ylabel('YLabel0')
ax.set_xlabel('XLabel0')

fig.suptitle('matplotlib.figure.Figure.suptitle() function Example\n\n', fontweight ="bold")

plt.show()
