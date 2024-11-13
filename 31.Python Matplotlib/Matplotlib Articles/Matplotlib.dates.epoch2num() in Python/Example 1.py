import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# generate some random data
# for approx 5 yrs
random_data = [float(random.randint(1487517521,
									14213254713))
			for _ in range(1000)]

# convert the epoch format to
# matplotlib date format
mpl_data = mdates.epoch2num(random_data)

# plotting the graph
fig, axes = plt.subplots(1, 1)
axes.hist(mpl_data, bins = 51, color ='green')
locator = mdates.AutoDateLocator()

axes.xaxis.set_major_locator(locator)
axes.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))

plt.show()
