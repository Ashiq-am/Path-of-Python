# importing pandas as pd
import pandas as pd

# sample dataframe
df = pd.DataFrame({
	'A': [1, 2, 3, 4, 5],
	'B': ['a', 'b', 'c', 'd', 'e'],
	'C': [1.1, 2.1, 3.0, 4.1, 5.1]
	}, dtype ='object')

# converting datatypes
df = df.infer_objects()
print(df.dtypes)
