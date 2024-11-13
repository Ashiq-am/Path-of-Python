# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import numpy as np


fig, ax1 = plt.subplots()
ax1.imshow([[1, 2], [2, 3]])
txt = ax1.annotate("Fourth",
				(1., 1.),
				(0., 0),
				arrowprops=dict(arrowstyle="->",
								connectionstyle="angle3",
								lw=2),
				size=20,
				ha="center",
				path_effects=[PathEffects.withStroke(linewidth=3,
														foreground="g")])

txt.arrow_patch.set_path_effects([
	PathEffects.Stroke(linewidth=5, foreground="purple"),
	PathEffects.Normal()])

ax1.grid(True, linestyle="-")

pe = [PathEffects.withStroke(linewidth=3,
							foreground="purple")]

for l in ax1.get_xgridlines() + ax1.get_ygridlines():
	l.set_path_effects(pe)

print("Value Return by get_path_effects() : \n")

for l in ax1.get_xgridlines() + ax1.get_ygridlines():
	for i in Tick.get_path_effects(l):
		print(i)

fig.suptitle("""matplotlib.axis.Tick.get_path_effects()
function Example\n""", fontweight="bold")

plt.show()
