import pandas as pd
import numpy as np


data = np.array(['ant','bat','cat','dog'])
series = pd.Series(data,index=[100,101,102,103])
print(series)
print(type(series))

print("\nConvert Pandas Series to Python list")
print(series.tolist())
print(type(series.tolist()))
