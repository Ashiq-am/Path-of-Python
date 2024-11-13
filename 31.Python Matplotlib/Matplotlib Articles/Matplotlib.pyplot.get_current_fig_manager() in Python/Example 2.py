# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)

w = plt.get_current_fig_manager()

print("Value Return by get_current_fig_manager():")
print(w)

fig.suptitle('matplotlib.pyplot.get_current_fig_manager()\
function Example', fontweight="bold")

plt.show()
