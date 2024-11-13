# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects


fig, ax = plt.subplots()
t = ax.text(0.02, 0.5,
			'GeeksForGeeks',
			fontsize = 40,
			weight = 1000,
			va ='center')

t.set_path_effects([path_effects.PathPatchEffect(offset =(4, -4),
												hatch ='xxxx',
												facecolor ='gray'),
					path_effects.PathPatchEffect(edgecolor ='white',
												linewidth = 1.1,
												facecolor ='black')])

fig.suptitle('matplotlib.axes.Axes.set_path_effects() function Example\n', fontweight ="bold")

plt.show()
