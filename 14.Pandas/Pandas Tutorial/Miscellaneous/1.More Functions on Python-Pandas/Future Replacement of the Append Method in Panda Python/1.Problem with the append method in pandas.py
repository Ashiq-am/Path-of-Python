#Import panda module in your python code
import pandas as pd
#Create two Series
series1 = pd.Series([1,-2,3,4,-3,9,-74])
series2 = pd.Series([1,2,3,4,3,9,74])
#Concatenate two series with append()
series3 = series2.append(series1)
print(series3)
