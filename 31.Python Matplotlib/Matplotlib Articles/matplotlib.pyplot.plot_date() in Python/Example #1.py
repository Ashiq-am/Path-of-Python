# Implementation of matplotlib function
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import drange
import numpy as np

date1 = datetime.datetime(2020, 4, 2)
date2 = datetime.datetime(2020, 4, 12)
delta = datetime.timedelta(hours = 24)
dates = drange(date1, date2, delta)

y = np.arange(len(dates))

plt.plot_date(dates, y ** 2)
plt.title('matplotlib.pyplot.plot_date() function Example', fontweight ="bold")
plt.show()
