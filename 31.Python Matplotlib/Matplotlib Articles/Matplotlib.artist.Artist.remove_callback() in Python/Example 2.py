# Implementation of matplotlib function
from random import randint, choice
import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches

back_color = "black"
colors = ['red', 'green', 'blue', 'purple']
width, height = 4, 4

fig = plt.figure()
plt.xlim([0, width])
plt.ylim([0, height])

fig.canvas.draw()

it = 1


def update():
    global it
    x = randint(0, width - 1)
    y = randint(0, height - 1)

    arti = mpatches.Rectangle(
        (x, y), 1, 1,
        facecolor=choice(colors),
        edgecolor=back_color
    )

    fig.add_artist(arti)
    fig.draw_artist(arti)
    fig.canvas.blit(fig.bbox)

    if it > 100:
        timer.remove_callback(w)
    it += 1


timer = fig.canvas.new_timer(interval=1)
w = timer.add_callback(update)
timer.start()

fig.suptitle('matplotlib.artist.Artist.remove_callback() \
function Example', fontweight="bold")

plt.show()
