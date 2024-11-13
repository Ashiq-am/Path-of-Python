# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(np.random.rand(10))

def onclick(event):
	print('% s click: button =% d, x =% d, y =% d,xdata =% f, ydata =% f' %
		('double' if event.dblclick else 'single',
		event.button,
		event.x,
		event.y,
		event.xdata,
		event.ydata))

cid = fig.canvas.mpl_connect('button_press_event',
							onclick)
fig.canvas.mpl_disconnect(cid)

plt.suptitle('matplotlib.pyplot.disconnect() function Example', fontweight ="bold")

plt.show()
