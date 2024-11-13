# Implementation of matplotlib function
from random import randint, choice
import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

back_color = "black"
colors = ['red', 'green', 'blue', 'purple']
width, height = 4, 4

fig = plt.figure()
plt.xlim([0, width])
plt.ylim([0, height])

fig.canvas.draw()


def update():
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
    print("Draw at time :", time.time())


timer = fig.canvas.new_timer(interval=1)
timer.add_callback(update)
timer.start()

fig.suptitle('matplotlib.artist.Artist.add_callback() \
function Example', fontweight="bold")

plt.show()
