import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator


x = np.linspace(0, 10, 10)
y = 2**x

f = plt.figure()
ax = f.add_subplot(111)
plt.yscale('log')

ax.yaxis.set_major_locator(LogLocator(base = 100))

ax.plot(x, y)

plt.show()
