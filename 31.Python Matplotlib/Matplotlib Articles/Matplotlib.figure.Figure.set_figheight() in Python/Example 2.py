# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

fig = plt.figure(figsize=(7, 6))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

xx = np.arange(0, 2 * np.pi, 0.01)
ax.plot(xx, np.sin(xx))

fig.set_figheight(4.8)

fig.suptitle("""matplotlib.figure.Figure.set_figheight() 
function Example\n\n""", fontweight="bold")

plt.show()
