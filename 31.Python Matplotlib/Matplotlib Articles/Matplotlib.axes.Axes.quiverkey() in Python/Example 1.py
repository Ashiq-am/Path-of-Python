# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
ax.quiverkey(q, X=0.5, Y=0.5, U=500,
             label='Quiver key')

ax.set_title('matplotlib.axes.Axes.quiverkey() \
Example', fontsize=14, fontweight='bold')
plt.show()
