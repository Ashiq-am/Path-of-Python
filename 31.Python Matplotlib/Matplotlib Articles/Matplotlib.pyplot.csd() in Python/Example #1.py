# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))
nse2 = np.random.randn(len(t))

s1 = 1.5 * np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.cos(np.pi * t) + nse2

plt.csd(s1, s2**2, 128, 1./dt)
plt.xlabel('Frequency')
plt.ylabel('CSD(db)')

plt.title('matplotlib.pyplot.csd() function Example',
		fontweight ="bold")

plt.show()
