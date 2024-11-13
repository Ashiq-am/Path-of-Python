# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-2, 3, .01)
s = np.sin(np.pi * t)

plt.plot(t, s, color='black')
plt.axhline(y=1, color='black')

plt.axvline(x=1, color='black')
plt.axvline(x=0.5, ymin=0.75, linewidth=8,
            color='green')

plt.axhline(y=.5, xmin=0.25, xmax=0.75,
            color='black')

plt.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
plt.axvspan(2.25, 2.55, facecolor='green', alpha=0.5)

plt.title('matplotlib.pyplot.axhspan() Example\n',
          fontsize=14, fontweight='bold')

plt.show()
