# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20, 0.005)
y = 3.5 * np.exp(-x / 3.) * np.sin(2 * np.pi * x)

fig, ax = plt.subplots()
ax.plot(x, y, color ="green")
ax.set_xlim(0, 20)
ax.set_ylim(-4, 4)

xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata,
											ydata))

bbox = dict(boxstyle ="round", fc ="0.8")
arrowprops = dict(arrowstyle = "->", connectionstyle = "angle, angleA = 0, angleB = 90, rad = 10")

offset = 72

# Annotation
ax.annotate('data = (%.1f, %.1f)'%(xdata, ydata),
			(xdata, ydata), xytext =(-2 * offset,
									offset),
			textcoords ='offset points',
			bbox = bbox, arrowprops = arrowprops)


ax.annotate('display = (%.1f, %.1f)'%(xdisplay, ydisplay),
			(xdisplay, ydisplay), xytext =(0.5 * offset,
										-offset),
			xycoords ='figure pixels',
			textcoords ='offset points',
			bbox = bbox, arrowprops = arrowprops)

ax.set_title('matplotlib.axes.Axes.annotate() Example')
plt.show()
