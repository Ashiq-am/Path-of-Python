# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U = np.cos(X ** 2)
V = np.sin(Y ** 2)
C = U ** 2 + V ** 2

Q = plt.quiver(X, Y, U, V, C, units='width')
plt.quiverkey(Q, 0.4, 0.9, 1,
              r'val = $Cos(x ^ 2)^2 + Sin(x ^ 2)^2$',
              labelpos='E',
              coordinates='figure')

plt.title('matplotlib.pyplot.quiverkey() Example\n',
          fontsize=14, fontweight='bold')

plt.show()
