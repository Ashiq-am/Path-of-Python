from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import signal

# Creating 3D figure
fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection = '3d')

# Creating Dataset
color_cycle = plt.rcParams['axes.prop_cycle']()
x = linspace(0, 1, 51)
a = x*( 1 - x)
b = 0.25 - a
c = x*x*(1 - x)
d = 0.25-c

ax.plot3D(x, a, **next(color_cycle))

# 360 Degree view
for angle in range(0, 360):
    ax.view_init(angle, 30)
    plt.draw()
    plt.pause(.001)

plt.show()
