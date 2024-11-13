# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import numpy as np

fig, ax1 = plt.subplots()
ax1.imshow([[1, 2], [2, 3]])

txt = ax1.annotate("Fourth Qaud",
                   (1., 1.),
                   (0., 0),
                   arrowprops=dict(arrowstyle="->",
                                   connectionstyle="angle3",
                                   lw=2),
                   size=20, ha="center",
                   path_effects=[PathEffects.withStroke(linewidth=3,
                                                        foreground="w")])

Artist.set_path_effects(txt.arrow_patch, [
    PathEffects.Stroke(linewidth=5,
                       foreground="w"),
    PathEffects.Normal()])

ax1.grid(True, linestyle="-")

pe = [PathEffects.withStroke(linewidth=3,
                             foreground="w")]

for l in ax1.get_xgridlines() + ax1.get_ygridlines():
    Artist.set_path_effects(l, pe)

fig.suptitle('matplotlib.artist.Artist.set_path_effects()\
function Example', fontweight="bold")

plt.show()
