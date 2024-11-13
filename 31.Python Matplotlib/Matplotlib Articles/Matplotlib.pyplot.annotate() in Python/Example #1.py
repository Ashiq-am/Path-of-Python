# Implementation of matplotlib.pyplot.annotate()
# function

import matplotlib.pyplot as plt
import numpy as np


fig, geeeks = plt.subplots()

t = np.arange(0.0, 5.0, 0.001)
s = np.cos(3 * np.pi * t)
line = geeeks.plot(t, s, lw = 2)

# Annotation
geeeks.annotate('Local Max', xy =(3.3, 1),
				xytext =(3, 1.8),
				arrowprops = dict(facecolor ='green',
								shrink = 0.05),)

geeeks.set_ylim(-2, 2)

# Plot the Annotation in the graph
plt.show()
