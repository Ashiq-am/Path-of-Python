# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

fig, geeeks = plt.subplots()

t = np.arange(0.0, 5.0, 0.001)
s = np.cos(3 * np.pi * t)
line = geeeks.plot(t, s, lw=2)

# Annotation
geeeks.annotate('Local Max', xy=(3.3, 1),
                xytext=(3, 1.8),
                arrowprops=dict(facecolor='green',
                                shrink=0.05), )

geeeks.set_ylim(-2, 2)
fig.suptitle('Matplotlib.axis.Axis.get_offset_text()\n\
Function Example')
geeeks.grid()

print("Value of get_offset_text() :", geeeks.xaxis.get_offset_text())

plt.show()
