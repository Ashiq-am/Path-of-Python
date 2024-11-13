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
ax.plot(y, x)
ax.set_ylabel('Degree')
ax.set_xlabel('Frequency')


def val1(y):
	return y * np.pi / 180


def val2(y):
	return y * 180 / np.pi

secax = ax.secondary_yaxis('right', functions =(val1, val2))
secax.set_ylabel('Radian')
ax.set_title('matplotlib.axes.Axes.secondary_yaxis() Example',
			fontsize = 14, fontweight ='bold')
plt.show()
