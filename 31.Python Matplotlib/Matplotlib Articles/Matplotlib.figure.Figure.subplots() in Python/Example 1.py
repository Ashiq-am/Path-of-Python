# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x**2)

fig = plt.figure()
ax = fig.subplots()

ax.plot(x, y)

fig.suptitle("""matplotlib.figure.Figure.subplots() 
function Example\n\n""", fontweight ="bold")

fig.show()
