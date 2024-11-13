# Implementation of matplotlib spy function
import matplotlib.pyplot as plt
import numpy as np


x = np.random.randn(50, 50)

x[15, :] = 0.
x[:, 40] = 0.

plt.spy(x)
