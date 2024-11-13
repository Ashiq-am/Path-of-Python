# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

# make an agg figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 7], [1, 5, 6, 9])


def format_coord(x=7, y=9):
    col = int(x + 0.5)
    row = int(y + 0.5)
    if col >= 0 and col < 5 and row >= 0 and row < 5:
        z = row + col
        return 'x =% 1.4f, y =% 1.4f, z =% 1.4f' % (x, y, z)
    else:
        return 'x =% 1.4f, y =% 1.4f' % (x, y)


ax.format_coord = format_coord

fig.suptitle('matplotlib.axes.Axes.format_coord()\
function Example', fontweight="bold")
plt.show()
