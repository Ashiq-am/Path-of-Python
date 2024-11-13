# Implementation of matplotlib function
import matplotlib.pyplot as plt

ax = plt.axes()
ax.arrow(0, 0, 0.6, 0.7, head_width = 0.05,
		head_length = 0.1)

ax.set_title('matplotlib.axes.Axes.arrow() Example',
			fontsize = 14, fontweight ='bold')

plt.show()
