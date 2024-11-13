# implementation of the matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.arange(100)
x, y = np.meshgrid(dots, dots)

data = [x.ravel(), y.ravel()]
ax.scatter(*data, c=data[1])

with plt.rc_context({'axes.autolimit_mode': 'round_numbers',
                     'axes.xmargin': .8,
                     'axes.ymargin': .8}):
    fig, ax = plt.subplots()
    ax.scatter(*data, c=data[1])

plt.grid(True)

plt.title('matplotlib.pyplot.rc_context() Example')
plt.show()
