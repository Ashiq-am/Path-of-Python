# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(2, 2)

ax = fig.add_subplot(gs[0, :])
ax.plot(np.arange(0, 1e6, 1000))

ax.set_ylabel('YLabel0')
ax.set_xlabel('XLabel0')

for i in range(2):
    ax = fig.add_subplot(gs[1, i])
    ax.plot(np.arange(1., 0., -0.1) * 2000.,
            np.arange(1., 0., -0.1))

    ax.set_ylabel('YLabel1 % d' % i)
    ax.set_xlabel('XLabel1 % d' % i)

    if i == 0:
        for tick in ax.get_xticklabels():
            tick.set_rotation(55)

fig.align_xlabels()

fig.suptitle('matplotlib.figure.Figure.align_xlabels() \
function Example\n\n', fontweight="bold")

plt.show()
