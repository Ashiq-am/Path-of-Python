# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y1 = -3 * x*x + 10 * x + 10
y2 = 3 * x*x + x

fig, ax = plt.subplots()
ax.plot(x, y1, x, y2, color ='black')
ax.fill_between(x, y1, y2, where = y2 >y1,
			facecolor ='green', alpha = 0.8)
ax.fill_between(x, y1, y2, where = y2 <= y1,
			facecolor ='black', alpha = 0.8)

ax.set_frame_on(False)
x = ax.get_frame_on()
ax.text(-2, 80, "Value of set_frame_on : " +str(x),
		style ='italic', fontsize = 10, color ="green")
ax.set_title('matplotlib.axes.Axes.get_frame_on() Example\n', fontsize = 12, fontweight ='bold')
plt.show()
