# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 500)
y = np.sin(x**2)+np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y, label ='Line 1')

ax.plot(x, y - 0.6, label ='Line 2')

ax.legend()

fig.suptitle("""matplotlib.figure.Figure.show() 
function Example\n\n""", fontweight ="bold")

fig.show()
