# Implementation of matplotlib function
import matplotlib.pyplot as plt

ax = plt.axes()
ax.arrow(6, 7, -2.5, -2.5, head_width = 0.5,
		head_length = 0.5, fc ='g', ec ='g')
ax.set_title('matplotlib.axes.Axes.arrow() Example',
			fontsize = 14, fontweight ='bold')

ax.set(xlim =(1, 10), ylim =(1, 10))
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")

plt.show()
