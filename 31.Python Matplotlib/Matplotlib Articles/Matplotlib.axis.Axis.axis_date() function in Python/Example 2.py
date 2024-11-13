# Implementation of matplotlib function
from matplotlib.axis import Axis
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import (
    DateFormatter, AutoDateLocator, AutoDateFormatter, datestr2num
)

days = [
    '30/01/2019',
    '31/01/2019',
    '01/02/2019',
    '02/02/2019',
    '03/02/2019',
    '04/02/2019'
]
data1 = [2, 5, 13, 6, 11, 7]
data2 = [6, 3, 10, 3, 6, 5]

z = datestr2num([
    datetime.strptime(day, '%d/%m/%Y').strftime('%m/%d/%Y')
    for day in days
])

r = 0.25

figure = plt.figure(figsize=(8, 4))
axes = figure.add_subplot(111)

axes.bar(z - r, data1, width=2 * r,
         color='g', align='center',
         tick_label=days)
axes.bar(z + r, data2, width=2 * r,
         color='y', align='center',
         tick_label=days)

axes.xaxis.axis_date()

plt.title("Matplotlib.axis.Axis.axis_date()\
Function Example", fontsize=12, fontweight='bold')

plt.show()
