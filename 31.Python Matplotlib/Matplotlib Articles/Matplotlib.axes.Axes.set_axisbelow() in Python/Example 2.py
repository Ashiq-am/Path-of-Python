# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# Random test data
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size = 100) for std in range(1, 6)]
labels = ['x1', 'x2', 'x3', 'x4', 'x5']

fig, ax = plt.subplots()

bplot = ax.boxplot(all_data,
					vert = True,
					patch_artist = True,
					labels = labels)
colors = ['lightpink', 'lightblue', 'lightgreen',
		"lightgrey", "yellow"]
for patch, color in zip(bplot['boxes'], colors):
	patch.set_facecolor(color)

ax.yaxis.grid(True, color ="green", lw = 2)
ax.set_axisbelow(False)
ax.set_xlabel('Samples')
ax.set_ylabel('Observed values')
ax.set_title('matplotlib.axes.Axes.set_axisbelow() Example\n', fontsize = 12, fontweight ='bold')
plt.show()
