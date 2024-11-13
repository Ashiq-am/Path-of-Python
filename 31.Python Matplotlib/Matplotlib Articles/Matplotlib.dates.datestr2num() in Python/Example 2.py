import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates


dates = ['1920-05-06',
		'1920-05-07',
		'1947-05-08',
		'1920-05-09']

converted_dates = matplotlib.dates.datestr2num(dates)

x_axis = (converted_dates)
y_axis = range(0, 4)

plt.plot_date( x_axis, y_axis, '-' )

plt.show()
