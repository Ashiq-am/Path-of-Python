import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


# create dummy data
x = ['str{}'.format(k) for k in range(20)]
y = np.random.rand(len(x))

# create an IndexFormatter
# with labels x
x_fmt = mpl.ticker.IndexFormatter(x)

fig,ax = plt.subplots()

ax.plot(y)

# set our IndexFormatter to be
# responsible for major ticks
ax.xaxis.set_major_formatter(x_fmt)
