import numpy as np
import pandas as pd

# loading dataset
data = pd.read_csv('path of dataset')

# setting the index for the data
data = data.set_index(['created_at'])

# converting index to datetime index
data.index = pd.to_datetime(data.index)

# Changing start time for each hour, by default start time is at 0th minute
data.resample('W', loffset='30Min30s').price.sum().head(2)
data.resample('W', loffset='30Min30s').price.sum().head(2)

# we can also aggregate it will show quantity added in each week
# as well as the total amount added in each week
data.resample('W', loffset='30Min30s').agg(
	{'price': 'sum', 'quantity': 'sum'}).head(5)
