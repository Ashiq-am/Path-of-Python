# importing the module
import pandas as pd

# creating the DataFrame
df = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
					'B': ['B0', 'B1', 'B2', 'B3']})
display('df:', df1)
# creating the Series
series = pd.Series([1, 2, 3, 4])
display('series:', series)

# concatenating
display('After concatenating:')
display(pd.concat([df, series],
				axis = 1))
