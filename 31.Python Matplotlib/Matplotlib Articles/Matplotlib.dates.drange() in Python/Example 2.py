import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

date = [datetime.datetime(2020, 8, 24, 0, 0),
		datetime.datetime(2020, 8, 23, 0, 0),
		datetime.datetime(2020, 8, 22, 0, 0),
		datetime.datetime(2020, 8, 21, 0, 0),
		datetime.datetime(2020, 8, 18, 0, 0),
		datetime.datetime(2020, 8, 17, 0, 0),
		datetime.datetime(2020, 8, 16, 0, 0),
		datetime.datetime(2020, 8, 15, 0, 0),
		datetime.datetime(2020, 8, 14, 0, 0),
		datetime.datetime(2020, 8, 11, 0, 0),
		datetime.datetime(2020, 8, 10, 0, 0),
		datetime.datetime(2020, 8, 9, 0, 0),
		datetime.datetime(2020, 8, 8, 0, 0),
		datetime.datetime(2020, 8, 7, 0, 0),
		datetime.datetime(2020, 8, 4, 0, 0),
		datetime.datetime(2020, 8, 3, 0, 0),
		datetime.datetime(2020, 8, 2, 0, 0),
		datetime.datetime(2020, 8, 1, 0, 0)]

# is a datetime.datetime object
# according to type
start_date = date[0]

# is a datetime.datetime object according
# to type
end_date = date[-1]
delta = datetime.timedelta(days = 5)

# the drange function
dates = mdates.drange(start_date, end_date, -delta)
y_data = range(len(dates))

plt.plot(dates, y_data)
