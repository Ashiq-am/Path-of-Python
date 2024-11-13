# Initialising required libraries
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

# Loading the dataset
data = pd.read_csv("C:/Users/aparn/Desktop/data.csv")

# X axis is price_date
price_date = data['Date']

# Y axis is price closing
price_close = data['Close']

# Plotting the timeseries graph of given dataset
plt.plot(price_date, price_close)

# Giving title to the graph
plt.title('Prices by Date')

# rotating the x-axis tick labels at 30degree
# towards right
plt.xticks(rotation=30, ha='right')

# Giving x and y label to the graph
plt.xlabel('Price Date')
plt.ylabel('Price Close')
