# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1, 5, 0.1)
y = np.exp(-x)

yerr = 0.1 + 0.1 * np.sqrt(x)

fig, (ax, ax1) = plt.subplots(nrows = 1,
							ncols = 2,
							sharex = True)

ax.errorbar(x, y, yerr = yerr, color ="green")
ax.set_title('Title of Axes 1', fontweight ="bold")

ax1.errorbar(x, y, yerr = yerr, errorevery = 5,
			color ="green")
ax1.set_title('Title of Axes 2', fontweight ="bold")

w = ax.get_title()
ww = ax1.get_title()
ax.set_title("")
ax1.set_title("")

ax.set_xlabel(w)
ax1.set_xlabel(ww)

fig.suptitle("Previously assigned title of each Axes is used at labels\n", fontweight ="bold")
plt.show()
