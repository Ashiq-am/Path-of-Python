from pylab import *
import matplotlib
import matplotlib.ticker as ticker

# Setting minor ticker size to 0,
# globally.
matplotlib.rcParams['xtick.minor.size'] = 0

# Create a figure with just one
# subplot.
fig = figure()
ax = fig.add_subplot(111)

# Set both X and Y limits so that
# matplotlib
ax.set_xlim(0, 800)

# Fixes the major ticks to the places
# where desired (one every hundred units)
ax.xaxis.set_major_locator(ticker.FixedLocator(range(0,
                                                     801,
                                                     100)))
ax.xaxis.set_major_formatter(ticker.NullFormatter())

# Add minor tickers AND labels for them
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(n=2))
ax.xaxis.set_minor_formatter(ticker.FixedFormatter(['AB %d' % x
                                                    for x in range(1, 9)]))

ax.set_ylim(-2000, 6500, auto=False)

# common attributes for the bar plots
bcommon = dict(
    height=[8500],
    bottom=-2000,
    width=100)

bars = [[600, 'green'],
        [700, 'red']]
for left, clr in bars:
    bar([left], color=clr, **bcommon)

show()
