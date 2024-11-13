#import modules
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# Let say we have a dataframe of the days of
# the week and number of classes in each day of the upcoming week.
# Taking 7 days from 1-11-2021 to 7-11-2021

dataframe = pd.DataFrame({'date_of_week': np.array([datetime.datetime(2021, 11, i+1)
													for i in range(7)]),
						'classes': [5, 6, 8, 2, 3, 7, 4]})

# To draw scatter time series plot of the given dataframe
plt.plot_date(dataframe.date_of_week, dataframe.classes)

# rotating the x-axis tick labels at 30degree towards right
plt.xticks(rotation=30, ha='right')

# Giving title to the chart using plt.title
plt.title('Classes by Date')

# Providing x and y label to the chart
plt.xlabel('Date')
plt.ylabel('Classes')
