# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt


def GFG(n, m):
    def geeks(a):
        x = 1 / (.1 + np.random.random())
        y = 2 * np.random.random() - .5
        z = 10 / (.1 + np.random.random())

        for i in range(m):
            w = (i / m - y) * z
            a[i] += x * np.exp(-w * w)

    a = np.zeros((m, n))

    for i in range(n):
        for j in range(5):
            geeks(a[:, i])

    return a


test = GFG(3, 100)

fig, ax = plt.subplots()
ax.stackplot(range(100), test.T,
             baseline='wiggle')

ax.set_title('matplotlib.axes.Axes.stackplot Example')
plt.show()
