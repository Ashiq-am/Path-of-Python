import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import numpy as np


date_1 = datetime.datetime( 2020, 3, 2)
date_2 = datetime.datetime( 2020, 10, 10)

time_delta = datetime.timedelta(days = 28)
dates = drange(date_1, date_2, time_delta)

y_axis = np.arange( len(dates) )

fig, ax = plt.subplots()
ax.plot_date(dates, y_axis * y_axis)

ax.xaxis.set_major_formatter( DateFormatter('% Y-% m') )

plt.show()
