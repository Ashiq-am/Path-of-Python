# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y = np.sin(x ** 2) + np.cos(x)

plt.plot(x, y, label='Line 1')

plt.plot(x, y - 0.6, label='Line 2')

w = plt.get_fignums()

plt.text(2, 1.98,
         "List of existing figure numbers : "
         + str(w),
         fontsize=12)

plt.title('matplotlib.pyplot.get_fignums() function\
Example', fontweight="bold")

plt.show()
