# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)

w = ax.properties()
print("Display all Properties\n")
for i in w:
    print(i, ":", w[i])

fig.suptitle('matplotlib.axes.Axes.properties()\
function Example', fontweight="bold")

plt.show()
