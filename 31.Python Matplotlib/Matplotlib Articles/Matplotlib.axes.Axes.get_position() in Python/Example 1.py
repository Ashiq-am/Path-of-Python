# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = [2, 4, 6, 14, 15, 16, 17, 16, 18, 20]
y2 = [10, 11, 12, 13, 8, 10, 12, 14, 18, 19]

fig, ax1 = plt.subplots()

ax1.plot(x, y, "go-", label ='Line 1', )
ax1.plot(x, y2, "o-", label ='Line 2')

chartBox = ax1.get_position()
x, y, w, h = chartBox.x0, chartBox.y0, chartBox.width, chartBox.height

ax1.text(0, 20, "Bbox - xmin : "+str(x),
		fontweight ="bold")
ax1.text(0, 19, "Bbox - ymin : "+str(round(y, 2)),
		fontweight ="bold")
ax1.text(0, 18, "Bbox - width : "+str(w),
		fontweight ="bold")
ax1.text(0, 17, "Bbox - height : "+str(h),
		fontweight ="bold")
fig.suptitle('matplotlib.axes.Axes.get_position() function Example\n', fontweight ="bold")
plt.show()
