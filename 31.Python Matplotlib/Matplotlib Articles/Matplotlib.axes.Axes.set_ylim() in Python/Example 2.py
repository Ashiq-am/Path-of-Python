# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
ax1.set(xlim =(-0.5, 1.5), ylim =(-0.5, 1.5),
			autoscale_on = False)
ax2.set(xlim =(0.5, 0.75), ylim =(0.5, 0.75),
			autoscale_on = False)

x, y, s, c = np.random.rand(4, 200)
s *= 200

ax1.scatter(x, y, s, c)
ax2.scatter(x, y, s, c)


def GFG(event):
	if event.button != 1:
		return
	x, y = event.xdata, event.ydata
	ax2.set_xlim(x - 0.1, x + 0.1)
	ax2.set_ylim(y - 0.1, y + 0.1)
	fig2.canvas.draw()

fig1.canvas.mpl_connect('button_press_event', GFG)
ax1.set_title('matplotlib.axes.Axes.set_ylim() Example\n Original Window ',
			fontsize = 14, fontweight ='bold')
ax2.set_title('Zoomed window ',
			fontsize = 14, fontweight ='bold')
plt.show()
