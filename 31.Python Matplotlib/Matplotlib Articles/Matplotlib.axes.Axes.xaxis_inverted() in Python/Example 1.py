# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.axvspan(1.5, 2.5, facecolor ='g', alpha = 0.7)
ax.invert_xaxis()

ax.set_title('matplotlib.axes.Axes.xaxis_inverted() Example\n',
			fontsize = 14, fontweight ='bold')
x = ax.xaxis_inverted()
ans ="No"
if x:
	ans ="Yes"
ax.text(2.2, 1.02, "X-axis is inverted ? : " + ans,
		style ='italic', fontsize = 12)

plt.show()
