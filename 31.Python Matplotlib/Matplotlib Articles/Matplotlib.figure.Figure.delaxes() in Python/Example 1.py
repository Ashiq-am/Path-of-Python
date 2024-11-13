# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# make an agg figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3])

fig.delaxes(ax)

fig.suptitle('matplotlib.figure.Figure.delaxes() \
function Example\n\n', fontweight="bold")

plt.show()
