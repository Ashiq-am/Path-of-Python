# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-10, 10, 100)
sig = 1 / t**2
fig, ax = plt.subplots()

plt.axvline(color ="green", alpha = 0.8, lw = 1.5)
plt.plot(t, sig, linewidth = 1.5, color ="black",
		alpha = 0.6,
		label = r"$\sigma(t) = \frac{1}{x ^ 2}$")

plt.xlim(-10, 10)
plt.xlabel("t")
plt.legend(fontsize = 14)

ax.set_title('matplotlib.axes.Axes.axvline() Example')
plt.show()
