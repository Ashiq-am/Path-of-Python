# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(constrained_layout=True)
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Random spectrum')


def forward(x):
    return 1 / x


def inverse(x):
    return 1 / x


ax.set_title('matplotlib.axes.Axes.loglog Example2')
plt.show()
