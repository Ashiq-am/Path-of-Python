# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# creating a dataframe
data = pd.DataFrame({'Date': [datetime(2020, 6, 30),
                              datetime(2020, 7, 22),
                              datetime(2020, 8, 3),
                              datetime(2020, 9, 14)],

                     'Close': [8800, 2600, 8500, 7400]})

# x-axis
price_date = data['Date']

# y-axis
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='--', color='r')
plt.title('Market', fontweight="bold")
plt.xlabel('Date of Closing')
plt.ylabel('Closing Amount')

# Changing the formate of the date using
# dateformatter class
format_date = mpl_dates.DateFormatter('%d-%m-%Y')

# getting the accurate current axes using gca()
plt.gca().xaxis.set_major_formatter(format_date)

plt.show()
