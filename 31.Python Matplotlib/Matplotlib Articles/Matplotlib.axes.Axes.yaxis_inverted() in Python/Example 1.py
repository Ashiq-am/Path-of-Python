# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.axvspan(1.5, 2.5, facecolor ='g', alpha = 0.7)
ax.invert_yaxis()

ax.set_title('matplotlib.axes.Axes.yaxis_inverted() Example\n',
			fontsize = 14, fontweight ='bold')
x = ax.yaxis_inverted()
ans ="No"
if x:
	ans ="Yes"
ax.text(1.8, -0.02, "Y-axis is inverted ? : " + ans,
		style ='italic', fontsize = 12)

plt.show()
