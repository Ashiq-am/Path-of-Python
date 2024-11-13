# Implementation of matplotlib function
from matplotlib.axis import Axis
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MinuteLocator

x = [16.7,16.8,17.1,17.4]
y = [15,17,14,16]
plt.plot(x, y)

plt.gca().yaxis.axis_date()

plt.title("Matplotlib.axis.Axis.axis_date() Function Example", fontsize = 12, fontweight ='bold')

plt.show()
