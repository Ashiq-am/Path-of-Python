# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10**5)


dt = 0.0001
Fs = 1 / dt
geeks = np.array([22.00, 61.90, 7.80,
				24.40, 110.25, 20.05,
				15.00, 22.80, 34.90,
				57.30])

nse = np.random.randn(len(geeks))
r = np.exp(-geeks / 0.05)

s = 0.5 * np.sin(1.5 * np.pi * geeks) + nse

# plot phase_spectrum
fig, ax = plt.subplots()
ax.phase_spectrum(s, Fs = Fs, color ="green")

ax.set_title('matplotlib.axes.Axes.phase_spectrum() Example')

plt.show()
