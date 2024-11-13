# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 1.5 * np.pi, 100)
y = np.sin(x**2)+np.cos(x**2)

fig = plt.figure()
axs = fig.subplots(2, 2, subplot_kw = dict(polar = True))

axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

fig.suptitle("""matplotlib.figure.Figure.subplots() 
function Example\n\n""", fontweight ="bold")

fig.show()
