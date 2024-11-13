# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np


def samplemat(dims):
	"""Make a matrix with all zeros and increasing
	elements on the diagonal"""

	aa = np.zeros(dims)
	for i in range(min(dims)):
		aa[i, i] = np.sin(i**3)**2 + i**3
	return aa


# Display matrix
fig, ax = plt.subplots()
ax.matshow(samplemat((9, 9)), cmap ="Accent")

ax.set_title('matplotlib.axes.Axes.matshow() Examples\n')
plt.show()
