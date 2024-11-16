import pandas as pd


dti = pd.date_range('2020-07-01', periods = 4, freq ='M')
print(dti.month)
