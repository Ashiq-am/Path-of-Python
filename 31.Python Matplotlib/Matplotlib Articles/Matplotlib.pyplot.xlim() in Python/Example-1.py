# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

h = plt.plot(np.arange(0, 10), np.arange(0, 10))
plt.xlim([-5, 20])
l1 = np.array((1, 1))
angle = 65

th1 = plt.text(l1[0], l1[1], 'Line_angle',
			fontsize = 10, rotation = angle,
			rotation_mode ='anchor')

plt.title(" matplotlib.pyplot.xlim() Example")
plt.show()
