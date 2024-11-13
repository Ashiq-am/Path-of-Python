# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.cm as cm

from matplotlib.collections import LineCollection
from matplotlib.ticker import MultipleLocator


with cbook.get_sample_data('s1045.ima.gz') as dfile:
	im = np.frombuffer(dfile.read(),
					np.uint16).reshape((256, 256))

fig, ax1 = plt.subplots()
im = np.ravel(im)
im = im[np.nonzero(im)]
im = im / (2**20 - 1)
ax1.hist(im, bins = 40, color ="green")
ax1.set_yticks([])
ax1.set_xlabel('Intensity (a.u.)')
ax1.set_ylabel('MRI density')
ax1.minorticks_on()

fig.suptitle('matplotlib.axes.Axes.minorticks_on() function Example\n\n', fontweight ="bold")
plt.show()
