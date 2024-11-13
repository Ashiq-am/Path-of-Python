import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors, ticker


# helper function to
# show syslognorm in action
def symlog(arr, vmin=None, vmax=None,
           logthresh=5, logstep=1,
           linscale=1, **kwargs):
    vmin = arr.min() if vmin is None else vmin
    vmax = arr.max() if vmax is None else vmax
    image = plt.imshow(arr,
                       vmin=float(vmin),
                       vmax=float(vmax),
                       norm=colors.SymLogNorm(10 ** -logthresh,
                                              linscale=linscale),
                       **kwargs)

    maxlog = int(np.ceil(np.log10(vmax)))
    minlog = int(np.ceil(np.log10(-vmin)))

    # generate logarithmic ticks
    tick_locations = ([-(10 ** x) for x in range(-logthresh,
                                                 minlog + 1,
                                                 logstep)][::-1]
                      + [0.0]
                      + [(10 ** x) for x in range(-logthresh,
                                                  maxlog + 1,
                                                  logstep)])

    cb = plt.colorbar(ticks=tick_locations,
                      format=ticker.LogFormatter())

    return image, cb


data = np.arange(4).reshape(-1, 1) + np.arange(4).reshape(1, -1)
data = 10 ** (data / 2.)
data2 = data - data[::-1, ::-1]
plt.figure(figsize=(4, 3))
image, cb = symlog(data2, interpolation="None",
                   cmap="gray", logthresh=0)
plt.show()
