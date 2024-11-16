# importing the module
import pandas as pd

# creating the DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
					'B': ['B0', 'B1', 'B2', 'B3']})
display('df1:', df1)
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
					'B': ['B4', 'B5', 'B6', 'B7']})
display('df2:', df2)

# concatenating
display('After concatenating:')
display(pd.concat([df1, df2],
				ignore_index = True))
