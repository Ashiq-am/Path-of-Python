import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()


# helper function to plot the lines
def helper():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys


axes1 = plt.subplot2grid((7, 1), (0, 0),
                         rowspan=2,
                         colspan=1)

axes2 = plt.subplot2grid((7, 1), (2, 0),
                         rowspan=2,
                         colspan=1)

axes3 = plt.subplot2grid((7, 1), (4, 0),
                         rowspan=2,
                         colspan=1)

x, y = helper()
axes1.plot(x, y)

x, y = helper()
axes2.plot(x, y)

x, y = helper()
axes3.plot(x, y)
