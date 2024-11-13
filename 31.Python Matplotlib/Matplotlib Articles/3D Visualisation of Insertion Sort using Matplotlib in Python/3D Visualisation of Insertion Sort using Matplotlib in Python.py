# import the modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random

# Array size
n = 11


# insertion sort algorithm
def insertionsort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while (i >= 0 and a[i] > key):
            a[i + 1] = a[i]
            i -= 1
            yield a
        a[i + 1] = key

        yield a

    # method to plot graph


def showGraph(n):
    # for random unique values
    a = [i for i in range(1, n + 1)]
    random.shuffle(a)
    datasetName = 'Random'
    algoName = 'Insertion Sort'

    # generator object returned by the function
    generator = insertionsort(a)

    # the style of the graph
    plt.style.use('fivethirtyeight')

    # set bar colors
    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map",
        {
            "red": [(0, 1.0, 1.0),
                    (1.0, .5, .5)],
            "green": [(0, 0.5, 0.5),
                      (1.0, 0, 0)],
            "blue": [(0, 0.50, 0.5),
                     (1.0, 0, 0)]
        }
    )

    # plot the array
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # the z values and position of the bars
    z = np.zeros(n)
    dx = np.ones(n)
    dy = np.ones(n)
    dz = [i for i in range(len(a))]

    # plot 3d bars
    rects = ax.bar3d(range(len(a)), a, z, dx, dy, dz,
                     color=color_map(data_normalizer(range(n))))
    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(1.1 * len(a)))
    ax.set_title("ALGORITHM : " + algoName + "\n" + "DATA SET : " + datasetName,
                 fontdict={'fontsize': 13,
                           'fontweight': 'medium',
                           'color': '#E4365D'})

    # 2D text placed on the upper left
    # based on the axes fraction
    text = ax.text2D(0.1, 0.95, "",
                     horizontalalignment='center',
                     verticalalignment='center',
                     transform=ax.transAxes,
                     color="#E4365D")
    iteration = [0]

    # function for animating
    def animate(A, rects, iteration):
        # to clear the bars from the
        # Poly3DCollection object
        ax.collections.clear()
        ax.bar3d(range(len(a)), A, z, dx, dy, dz,
                 color=color_map(data_normalizer(range(n))))
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))

    anim = FuncAnimation(fig, func=animate,
                         fargs=(rects, iteration),
                         frames=generator, interval=50,
                         repeat=False)
    plt.show()


# Driver Code
showGraph(n)
