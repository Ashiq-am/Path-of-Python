# implementation of the matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

dots = np.arange(20)
x, y = np.meshgrid(dots, dots)
data = [x.ravel(), y.ravel()]

with plt.rc_context({'axes.xmargin': .2,
                     'axes.ymargin': .4}):
    plt.scatter(*data, c=data[1])

plt.grid(True)

plt.title('matplotlib.pyplot.rc_context()\
Example')
plt.show()
