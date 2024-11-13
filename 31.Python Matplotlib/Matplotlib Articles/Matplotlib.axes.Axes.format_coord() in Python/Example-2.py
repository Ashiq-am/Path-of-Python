# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


X = np.random.rand(15, 30)

fig, ax = plt.subplots()
ax.imshow(X)

val1, val2 = X.shape


def format_coord(x, y):
	col = int(x + 2)
	row = int(y - 2)
	if col >= 0 and col < val2 and row >= 0 and row < val1:
		z = X[row, col]
		return 'x =% 2.0f, y =% 2.0f, z =% 2.0f' % (x, y, z)
	else:
		return 'x =% 2.0f, y =% 2.0f' % (x, y)

ax.format_coord = format_coord

fig.suptitle('matplotlib.axes.Axes.format_coord() \
function Example', fontweight ="bold")
plt.show()
