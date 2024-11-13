# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

fig, ax4 = plt.subplots()

x = 10.0 ** np.linspace(0.0, 2.0, 15)
y = x ** 2.0
plt.xscale("log", nonposx='clip')
plt.yscale("log", nonposy='clip')

plt.errorbar(x, y, xerr=0.1 * x,
             yerr=2.0 + 1.75 * y,
             color="green")

plt.ylim(bottom=0.1)

plt.title('matplotlib.pyplot.xscale() \
function Example\n', fontweight="bold")

plt.show()
