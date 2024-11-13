# Implementation of matplotlib function
import numpy as np

np.random.seed(19680801)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for color in ['tab:green', 'tab:blue', 'tab:orange']:
    n = 70
    x, y = np.random.rand(2, n)
    scale = 1000.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.35)

fig.legend()
ax.grid(True)

fig.suptitle("""matplotlib.figure.Figure.legend() 
function Example\n\n""", fontweight="bold")

plt.show()
