import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ID': [10, np.nan, 20, 30, np.nan, 50, np.nan,
           150, 200, 102, np.nan, 130],

    'Sale': [10, 20, np.nan, 11, 90, np.nan,
             55, 14, np.nan, 25, 75, 35],

    'Date': ['2020-10-05', '2020-09-10', np.nan,
             '2020-08-17', '2020-09-10', '2020-07-27',
             '2020-09-10', '2020-10-10', '2020-10-10',
             '2020-06-27', '2020-08-17', '2020-04-25'],
})

df['Sale'].fillna(int(df['Sale'].mean()), inplace=True)
print(df)
