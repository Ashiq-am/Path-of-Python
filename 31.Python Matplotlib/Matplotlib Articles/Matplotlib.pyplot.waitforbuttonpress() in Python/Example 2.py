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


plt.clf()
ax.axis([-1., 1., -1., 1.])

plt.setp(plt.gca(), autoscale_on=False)

tellme("""matplotlib.pyplot.waitforbuttonpress() 
function Example\n\n""")

w = plt.waitforbuttonpress()
print("Result after click :", w)

plt.show()
