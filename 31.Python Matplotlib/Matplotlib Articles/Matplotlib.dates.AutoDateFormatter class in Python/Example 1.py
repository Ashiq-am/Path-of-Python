import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, AutoDateFormatter, date2num

# make my own data:
date = '2020-02-23'
low = 10

# how to format dates:
date_datetime = datetime.datetime.strptime(date, '% Y-% m-% d')
int_date = date2num( date_datetime)

# create plots:
figure, axes = plt.subplots()

# plot data:
axes.bar(int_date, low, label ="", color ="green")

# format date
locator = AutoDateLocator()
axes.xaxis.set_major_locator(locator)
axes.xaxis.set_major_formatter( AutoDateFormatter(locator) )

# apply autoformatter for displaying of dates
min_date = date2num( datetime.datetime.strptime('2020-02-16', '% Y-% m-% d') )
max_date = date2num( datetime.datetime.strptime('2020-02-28', '% Y-% m-% d') )
axes.set_xlim([min_date, max_date])
figure.autofmt_xdate()

# show plot:
plt.show()
