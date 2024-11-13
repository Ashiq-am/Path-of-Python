# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

fig = plt.figure(figsize=(5, 4))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

xx = np.arange(0, 2 * np.pi, 0.01)
ax.plot(xx, np.sin(xx))

fig.set_dpi(150.0)

fig.suptitle("""matplotlib.figure.Figure.set_dpi() 
function Example\n\n""", fontweight="bold")

plt.show()
