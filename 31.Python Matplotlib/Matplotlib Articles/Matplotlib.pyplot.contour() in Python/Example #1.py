# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib

delta = 0.15
x = np.arange(1.5, 2.5, delta)
y = np.arange(1.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z = (np.exp(X - Y))


CS1 = plt.contour(X, Y, Z)

fmt = {}
strs = ['1', '2', '3', '4', '5', '6', '7']
for l, s in zip(CS1.levels, strs):
	fmt[l] = s
plt.clabel(CS1, CS1.levels, inline = True,
		fmt = fmt, fontsize = 10)

plt.title('matplotlib.pyplot.contour() Example')
plt.show()
