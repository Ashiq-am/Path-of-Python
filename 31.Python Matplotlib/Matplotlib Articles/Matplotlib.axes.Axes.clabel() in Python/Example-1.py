# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib

delta = 2.5
x = np.arange(-13.0, 13.0, delta)
y = np.arange(-12.0, 12.0, delta)
X, Y = np.meshgrid(x, y)
Z = (np.exp(-X**2 - Y**2) - np.exp(-(X - 1)**2 - (Y - 1)**2)) * 3

fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['1', '2', '3', '4', '5', '6', '7']
for l, s in zip(CS1.levels, strs):
	fmt[l] = s
ax1.clabel(CS1, CS1.levels, inline = True,
		fmt = fmt, fontsize = 10)

ax1.set_title('matplotlib.axes.Axes.clabel() Example')
plt.show()
