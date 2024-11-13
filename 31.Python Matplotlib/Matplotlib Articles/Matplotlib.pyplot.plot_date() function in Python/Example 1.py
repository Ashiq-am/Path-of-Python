# importing libraries
import matplotlib.pyplot as plt
from datetime import datetime

# creating array of dates for x axis
dates = [
	datetime(2020, 6, 30),
	datetime(2020, 7, 22),
	datetime(2020, 8, 3),
	datetime(2020, 9, 14)
]

# for y axis
x = [0, 1, 2, 3]

plt.plot_date(dates, x, 'g')
plt.xticks(rotation=70)
plt.show()
