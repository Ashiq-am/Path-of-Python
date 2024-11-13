import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter

data = [8, 12, 15, 17, 18, 18.5]
perc = np.linspace(0, 100, len(data))

fig = plt.figure(1, (7, 4))
ax = fig.add_subplot(1, 1, 1)

ax.plot(perc, data)

xticks = mtick.PercentFormatter(0.5)
ax.xaxis.set_major_formatter(xticks)

plt.show()
