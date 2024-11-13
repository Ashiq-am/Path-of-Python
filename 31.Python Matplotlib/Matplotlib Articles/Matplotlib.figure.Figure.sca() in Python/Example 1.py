# Implementation of matplotlib function
import matplotlib.pyplot as plt
from scipy import sin, cos

fig, ax = plt.subplots(2, 1)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = sin(x)
y2 = cos(x)

fig.sca(ax[0])
plt.plot(x, y1)

fig.sca(ax[1])
plt.plot(x, y2)

fig.suptitle("""matplotlib.figure.Figure.sca() 
function Example\n\n""", fontweight="bold")

plt.show()
