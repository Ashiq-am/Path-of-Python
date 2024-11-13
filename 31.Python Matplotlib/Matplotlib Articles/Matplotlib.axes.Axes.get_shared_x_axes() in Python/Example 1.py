# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np


def GFG1(temp):
	return (5. / 9.) * (temp - 32)

def GFG2(ax1):
	y1, y2 = ax1.get_ylim()
	ax_twin .set_ylim(GFG1(y1), GFG1(y2))
	ax_twin .figure.canvas.draw()

fig, ax1 = plt.subplots()
ax_twin = ax1.twinx()

ax1.callbacks.connect("ylim_changed", GFG2)
ax1.plot(np.linspace(-40, 120, 100))
ax1.set_xlim(0, 100)

ax1.set_ylabel('Fahrenheit')
ax_twin .set_ylabel('Celsius')

w = ax1.get_shared_x_axes()
w1 = ax_twin.get_shared_x_axes()
for i in w:
	x, y = list(i)
	ax1.text(40, 100, "Value return : \n",
			fontweight ="bold")
	ax1.text(27, 90, str(x)+"\n"+str(y),
			fontweight ="bold")
fig.suptitle('matplotlib.axes.Axes.get_shared_x_axes() function Example\n\n', fontweight ="bold")
plt.show()
