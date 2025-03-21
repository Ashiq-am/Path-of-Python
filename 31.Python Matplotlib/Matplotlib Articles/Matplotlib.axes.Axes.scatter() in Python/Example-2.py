# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

# first define the ratios
r1 = 0.2
r2 = r1 + 0.3
r3 = r2 + 0.7

# define some sizes of the
# scatter marker
sizes = np.array([60, 80, 120, 50])

# calculate the points of the
# first pie marker
x1 = np.cos(2 * np.pi * np.linspace(0, r1))
y1 = np.sin(2 * np.pi * np.linspace(0, r1))

xy1 = np.row_stack([[0, 0],
                    np.column_stack([x1, y1])])

s1 = np.abs(xy1).max()

x2 = np.cos(2 * np.pi * np.linspace(r1, r2))
y2 = np.sin(2 * np.pi * np.linspace(r1, r2))

xy2 = np.row_stack([[0, 0],
                    np.column_stack([x2, y2])])

s2 = np.abs(xy2).max()

x3 = np.cos(2 * np.pi * np.linspace(r2, r3))
y3 = np.sin(2 * np.pi * np.linspace(r2, r3))
xy3 = np.row_stack([[0, 0],
                    np.column_stack([x3, y3])])

s3 = np.abs(xy3).max()

x4 = np.cos(2 * np.pi * np.linspace(r3, 1))
y4 = np.sin(2 * np.pi * np.linspace(r3, 1))
xy4 = np.row_stack([[0, 0],
                    np.column_stack([x4, y4])])

s4 = np.abs(xy4).max()

fig, ax = plt.subplots()
ax.scatter(range(3), range(3),
           marker=xy1, s=s1 ** 2 * sizes,
           facecolor='blue')

ax.scatter(range(3), range(3),
           marker=xy2, s=s2 ** 2 * sizes,
           facecolor='green')

ax.scatter(range(3), range(3),
           marker=xy3, s=s3 ** 2 * sizes,
           facecolor='red')

ax.scatter(range(3), range(3),
           marker=xy4, s=s4 ** 2 * sizes,
           facecolor='black')

ax.set_title("matplotlib.axes.Axes.scatter Example2")
plt.show()
