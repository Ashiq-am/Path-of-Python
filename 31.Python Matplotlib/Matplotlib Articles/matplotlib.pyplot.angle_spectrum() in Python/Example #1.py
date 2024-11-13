# Implementation of matplotlib.pyplot.angle_spectrum()
# function

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10**5)

dt = 0.0001
Fs = 1 / dt
geeks = np.array([24.40, 110.25, 20.05,
				22.00, 61.90, 7.80,
				15.00, 22.80, 34.90,
				57.30])

nse = np.random.randn(len(geeks))
r = np.exp(-geeks / 0.05)

s = 0.1 * np.sin(2 * np.pi * geeks) + nse

# plot angle_spectrum
plt.angle_spectrum(s, Fs = Fs)

# Display the simple spectrum and
# angle_spectrum plot
plt.show()
