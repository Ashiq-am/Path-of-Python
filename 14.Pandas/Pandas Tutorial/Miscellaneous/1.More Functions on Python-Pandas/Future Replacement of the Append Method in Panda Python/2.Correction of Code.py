#importing panda module in python program
import pandas as pd
series1 = pd.Series([1,-2,3,4,-3,9,-74])
series2 = pd.Series([1,2,3,4,3,9,74])
series3 = pd.concat([series2,series1],ignore_index=True)
series3
