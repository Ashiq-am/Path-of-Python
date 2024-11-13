# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)
import numpy as np
import datetime

np.random.seed(19680801)

Val1 = rrulewrapper(YEARLY, byeaster=1, interval=5)
Val2 = RRuleLocator(Val1)

formatter = DateFormatter('%y/%m/%d')

date1 = datetime.date(2000, 1, 1)
date2 = datetime.date(2014, 4, 12)
delta = datetime.timedelta(days=10)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))

fig, ax = plt.subplots()
plt.plot_date(dates, s, 'go')

ax.xaxis.set_major_locator(Val2)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=25,
                         labelsize=8,
                         labelcolor="g")
ax.yaxis.set_tick_params(rotation=25,
                         labelsize=12,
                         labelcolor="r")

plt.title('matplotlib.axis.Axis.set_tick_params()\n\
function Example', fontweight="bold")

plt.show()
