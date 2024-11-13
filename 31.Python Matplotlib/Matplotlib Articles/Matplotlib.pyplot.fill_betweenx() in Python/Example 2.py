import pylab as plt
import numpy as np

N = np.linspace(0,3,200)
A1 = N**2 + 3
A2 = np.exp(N) + 2
A3 = np.cos(N)

plt.plot(N, A1, lw = 3)
plt.plot(N, A2, lw = 3)
plt.plot(N, A3, lw = 3)

plt.fill_betweenx(N, A1, A2,
				color = 'r',
				alpha = .5)
plt.fill_betweenx(N, A1, A3,
				color = 'g',
				alpha = .5)

plt.show()
