# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects


fig, ax = plt.subplots()
t = ax.text(0.02, 0.5,
			'GeeksForGeeks',
			fontsize=40,
			weight=1000,
			va='center')

t.set_path_effects([path_effects.PathPatchEffect(offset=(4, -4),
												hatch='xxxx',
												facecolor='red'),
					path_effects.PathPatchEffect(edgecolor='white',
												linewidth=1.1,
												facecolor='purple')])

print("Value Return by get_path_effects() : \n")
for i in Tick.get_path_effects(t):
	print(i)

fig.suptitle("""matplotlib.axis.Tick.get_path_effects()
function Example\n""", fontweight="bold")

plt.show()
