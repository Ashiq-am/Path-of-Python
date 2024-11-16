# import pandas and numpy
import pandas as pd
import numpy as np

# Perform addition operation
a = pd.Series(pd.date_range('2020-8-10', periods=5, freq='D'))
b = pd.Series([pd.Timedelta(days=i) for i in range(5)])

gfg = pd.DataFrame({'A': a, 'B': b})
gfg['Result'] = gfg['A'] + gfg['B']

print(gfg)
