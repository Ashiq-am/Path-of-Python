# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
t = np.arange(0.01, 10.0, 0.001)
data1 = np.exp(t)
data2 = np.sin(0.4 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color = color)
ax1.plot(t, data1, color = color)
ax1.tick_params(axis ='y', labelcolor = color)

ax2 = ax1.twinx()

color = 'tab:green'
ax2.set_ylabel('sin', color = color)
ax2.plot(t, data2, color = color)
ax2.tick_params(axis ='y', labelcolor = color)

w = ax1.get_shared_x_axes()
w1 = ax2.get_shared_x_axes()
for i in w:
	x, y = list(i)
	ax1.text(4, 15000, "Value return : \n",
			fontweight ="bold")
	ax1.text(2, 13000, str(x)+"\n"+str(y),
			fontweight ="bold")
fig.suptitle('matplotlib.axes.Axes.get_shared_x_axes() function Example\n\n', fontweight ="bold")
plt.show()
