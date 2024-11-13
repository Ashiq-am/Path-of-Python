# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

fig = plt.figure()
gs = gridspec.GridSpec(2, 2)

for i in range(2):
	ax = fig.add_subplot(gs[1, i])
	ax.set_ylabel('Y label')
	ax.set_xlabel('X label')
	if i == 0:
		for tick in ax.get_xticklabels():
			tick.set_rotation(45)

fig.align_xlabels()

fig.suptitle('matplotlib.figure.Figure.align_xlabels() function Example\n\n', fontweight ="bold")

plt.show()
