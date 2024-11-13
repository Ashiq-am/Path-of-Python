import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker


xGrid = np.linspace(1-1e-14, 1-1e-16, 30,
					dtype = np.longdouble)

y = np.random.rand(len(xGrid))

plt.plot(xGrid, y)
plt.xlim(1-1e-14, 1)

loc = matplotlib.ticker.LinearLocator(numticks = 5)
plt.gca().xaxis.set_major_locator(loc)

plt.show()
