import numpy as np

import pandas as pd

# loading dataset

data = pd.read_csv(r'path of dataset')
# setting the index for the data
data = data.set_index(['created_at'])
# converting index to datetime index
data.index = pd.to_datetime(data.index)

# Changing start time for each hour, by default start time is at 0th minute
data.resample('W', loffset='30Min30s').price.sum().head(2)
data.resample('W', loffset='30Min30s').price.sum().head(2)

data.groupby([pd.Grouper(freq='M'), 'store_type']).agg(total_quantity=('quantity', 'sum'),
													total_amount=('price', 'sum')).head(5)
