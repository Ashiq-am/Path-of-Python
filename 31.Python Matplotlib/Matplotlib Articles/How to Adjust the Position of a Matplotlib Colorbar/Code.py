# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

# specify dimensions of colorbar using random module
Z = np.random.rand(5, 20)

fig, ax0 = plt.subplots()
ax0.pcolor(Z)

ax0.set_title('Matplotlib-colorbar')
plt.show()
