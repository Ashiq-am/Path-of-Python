# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
U, V = np.meshgrid(X, Y)

q = plt.quiver(X, Y, U, V)
plt.quiverkey(q, X=0.5, Y=0.5,
              U=500, label='Quiver key')

plt.title('matplotlib.pyplot.quiverkey() Example')

plt.show()
