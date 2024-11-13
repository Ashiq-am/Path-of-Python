# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)

w = fig.get_window_extent()

print("Value Return by get_window_extent():")
print(w)

fig.suptitle('matplotlib.figure.Figure.get_window_extent()\
function Example', fontweight="bold")

plt.show()
