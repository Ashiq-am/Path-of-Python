import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.0, 2.0, 401)
s = np.sin(2 * np.pi * t)

fig, [ax, ax1] = plt.subplots(2, 1)

ax.set_ylabel('y-axis')
ax.plot(t, s)
ax.grid(True)

ax1.set_ylabel('y-axis')
ax1.set_xlabel('x-axis')
ax1.plot(t, s)
ax1.grid(True)
# Function call
ax1.cla()

fig.suptitle('matplotlib.pyplot.cla Example')
plt.show()
