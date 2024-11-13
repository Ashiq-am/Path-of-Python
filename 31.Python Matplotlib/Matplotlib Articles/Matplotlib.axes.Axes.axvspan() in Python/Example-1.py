# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.axvspan(1.5, 2.5, facecolor ='g', alpha = 0.7)

ax.set_title('matplotlib.axes.Axes.axvspan() Example')

plt.show()
