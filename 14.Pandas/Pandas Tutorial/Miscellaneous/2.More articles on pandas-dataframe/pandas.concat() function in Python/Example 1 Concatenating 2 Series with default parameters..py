# importing the module
import pandas as pd

# creating the Series
series1 = pd.Series([1, 2, 3])
display('series1:', series1)
series2 = pd.Series(['A', 'B', 'C'])
display('series2:', series2)

# concatenating
display('After concatenating:')
display(pd.concat([series1, series2]))
