# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(4 * np.pi * x)

plt.minorticks_on()
plt.fill_between(x, y1, y2, color ="green", alpha = 0.6)
plt.minorticks_off()
plt.title('matplotlib.pyplot.minorticks_off() function Example',
											fontweight ="bold")
plt.show()
