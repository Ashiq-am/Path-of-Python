# importing the module
import pandas as pd

# creating the DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
					'B': ['B0', 'B1', 'B2', 'B3']})
display('df1:', df1)
df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
					'D': ['D0', 'D1', 'D2', 'D3']})
display('df2:', df2)

# concatenating
display('After concatenating:')
display(pd.concat([df1, df2],
				axis = 1))
