import pandas as pd
from datetime import datetime
import numpy as np

range_date = pd.date_range(start ='1/1/2019', end ='1/08/2019',
												freq ='Min')

df = pd.DataFrame(range_date, columns =['date'])
df['data'] = np.random.randint(0, 100, size =(len(range_date)))

print(df.head(10))
