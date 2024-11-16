import pandas as pd
from datetime import datetime
import numpy as np

range_data = pd.date_range(start ='1/1/2019', end ='1/08/2019',
												freq ='Min')

df = pd.DataFrame(range_data, columns =['date'])
df['data'] = np.random.randint(0, 100, size =(len(range_data)))

df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis = 1, inplace = True)

print(df['2019-01-05'][1:11])
