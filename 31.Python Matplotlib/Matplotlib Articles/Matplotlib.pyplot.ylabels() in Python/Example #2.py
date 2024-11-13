# Implementation of matplotlib.pyplot.ylabels()
# function

import numpy as np
import matplotlib.pyplot as plt

valx1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

valy1 = np.cos(2 * np.pi * valx1) * np.exp(-valx1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(valx1, valy1, 'o-')
plt.title('ylabel() Example')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()
