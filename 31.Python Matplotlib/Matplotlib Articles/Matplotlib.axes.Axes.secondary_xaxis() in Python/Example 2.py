# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
from matplotlib.transforms import Transform
from matplotlib.ticker import (
	AutoLocator, AutoMinorLocator)

fig, ax = plt.subplots(constrained_layout = True)
x = np.arange(0, 500, 2)
y = np.sin(3 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('Degree')
ax.set_ylabel('Frequency')


def val1(x):
	return x * np.pi / 180


def val2(x):
	return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions =(val1, val2))
secax.set_xlabel('Radian')
ax.set_title('matplotlib.axes.Axes.secondary_xaxis() Example',
			fontsize = 14, fontweight ='bold')
plt.show()
