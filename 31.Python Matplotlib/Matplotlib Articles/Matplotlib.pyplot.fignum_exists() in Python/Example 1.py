# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(20) / 50
y = (x + 0.1) * 3

val1 = [True, False] * 10
val2 = [False, True] * 10

plt.errorbar(x, y,
             xerr=0.1,
             xlolims=True,
             label='Line 1')

y = (x + 0.3) * 3

y = (x + 0.6) * 4

plt.errorbar(x + 1.2,
             y,
             xerr=0.1,
             xuplims=True,
             label='Line 3')

plt.legend()

plt.text(0.5, 3.7,
         "Figure 1 Exists ? " +
         str(plt.fignum_exists(1)),
         fontweight="bold")

plt.title('matplotlib.pyplot.fignum_exists()function\
Example', fontweight="bold")

plt.show()
