# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# Time series data
geeksx = np.array([24.40, 110.25, 20.05,
                   22.00, 61.90, 7.80,
                   15.00])

geeksy = np.array([24.40, 110.25, 20.05,
                   22.00, 61.90, 7.80,
                   15.00])

fig, ax = plt.subplots()
ax.xcorr(geeksx, geeksy, maxlags=6,
         color="green")

ax.set_axis_off()

ax.set_title('matplotlib.axes.Axes.set_axis_off()\
Example')
plt.show()
