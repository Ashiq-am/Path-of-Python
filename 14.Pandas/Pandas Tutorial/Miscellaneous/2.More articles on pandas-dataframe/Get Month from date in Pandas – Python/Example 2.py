import pandas as pd
import numpy as np
import datetime

date1 = pd.Series(pd.date_range('2020-7-1 12:00:00', periods = 5))
df = pd.DataFrame(dict(date_given = date1))

df['month_of_date'] = df['date_given'].dt.month
df
