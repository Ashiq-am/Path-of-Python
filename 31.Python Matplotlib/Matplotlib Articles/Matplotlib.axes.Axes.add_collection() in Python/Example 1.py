# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np

np.random.seed(19680801)
xvalue = np.random.random([2, 10])
xvalue1 = xvalue[0, :]
xvalue2 = xvalue[1, :]
xvalue1.sort()
xvalue2.sort()

yvalue1 = xvalue1 ** 4
yvalue2 = 1 - xvalue2 ** 6

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xvalue1, yvalue1, color ='tab:blue')
ax.plot(xvalue2, yvalue2, color ='tab:green')

xresult1 = EventCollection(xvalue1, color ='tab:blue')
xresult2 = EventCollection(xvalue2, color ='tab:green')
yresult1 = EventCollection(yvalue1, color ='tab:blue',
						orientation ='vertical')
yresult2 = EventCollection(yvalue2, color ='tab:green',
						orientation ='vertical')
ax.add_collection(xresult1)
ax.add_collection(xresult2)
ax.add_collection(yresult1)
ax.add_collection(yresult2)

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

fig.suptitle('matplotlib.axes.Axes.add_collection() function Example\n\n', fontweight ="bold")
plt.show()
