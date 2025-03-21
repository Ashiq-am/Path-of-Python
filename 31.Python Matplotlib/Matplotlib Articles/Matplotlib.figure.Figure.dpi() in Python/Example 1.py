# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()

nx = int(fig.get_figwidth() * fig.dpi)
ny = int(fig.get_figheight() * fig.dpi)

data = np.random.random((ny, nx))
plt.plot(data)

fig.suptitle('matplotlib.figure.Figure.dpi function Example', fontweight ="bold")

plt.show()
