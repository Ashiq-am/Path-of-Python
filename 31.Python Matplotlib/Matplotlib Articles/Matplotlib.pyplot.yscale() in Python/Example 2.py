import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

from docutils.nodes import inline

matplotlib
inline

# Example 2
# useful for `logit` scale
from matplotlib.ticker import NullFormatter

# Fixing random state for reproducibility
np.random.seed(100)

# make up some data in the
# interval ]0, 1[
y = np.random.normal(loc=0.5,
					scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# symmetric log
plt.subplot(221)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(222)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

plt.gca().yaxis.set_minor_formatter(NullFormatter())

# Adjust the subplot layout, because
# the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.80, bottom=0.03,
					left=0.15, right=0.92,
					hspace=0.34,wspace=0.45)

plt.show()
