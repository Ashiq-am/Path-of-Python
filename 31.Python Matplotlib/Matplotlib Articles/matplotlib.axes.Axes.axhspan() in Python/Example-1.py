# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.axhspan(1.25, 1.55, facecolor ='g', alpha = 0.5)

ax.set_title('matplotlib.axes.Axes.axhspan() Example')

plt.show()
