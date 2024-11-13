# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots()

x = np.random.randn(20, 50)
x[12, :] = 0.
x[:, 22] = 0.
ax1.spy(x)

plt.show()
ax1.set_title('matplotlib.axes.Axes.spy() Example')
plt.show()
