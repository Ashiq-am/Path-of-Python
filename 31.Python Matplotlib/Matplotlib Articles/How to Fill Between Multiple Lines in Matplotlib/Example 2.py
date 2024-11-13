import pylab as plt
import numpy as np

X = np.linspace(0, 3, 200)
Y1 = X**2 + 3
Y2 = np.sin(X)
Y3 = np.cos(X)

plt.plot(X, Y1, lw=4)
plt.plot(X, Y2, lw=4)
plt.plot(X, Y3, lw=4)

plt.fill_between(X, Y1, Y2, color='k', alpha=.5)
plt.fill_between(X, Y1, Y3, color='y', alpha=.5)

plt.show()
