# Implementation of matplotlib function
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.subplots()


def tellme(s):
    fig.suptitle(s, fontweight="bold")
    fig.canvas.draw()
    renderer = fig.canvas.renderer
    fig.draw(renderer)


fig.clf()
ax.axis([-1., 1., -1., 1.])
plt.setp(plt.gca(), autoscale_on=False)

tellme("""matplotlib.figure.Figure.waitforbuttonpress() 
	function Example\n\n""")

w = fig.waitforbuttonpress()
print("Result after click :", w)
fig.show()
