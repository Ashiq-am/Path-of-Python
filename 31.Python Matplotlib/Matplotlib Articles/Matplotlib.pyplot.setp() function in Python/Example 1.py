#Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt


def tellme(s):
	plt.title(s, fontsize=16)
	plt.draw()
plt.clf()
plt.setp(plt.gca(), autoscale_on=False)

tellme('matplotlib.pyplot.setp() function Example')
plt.show()
