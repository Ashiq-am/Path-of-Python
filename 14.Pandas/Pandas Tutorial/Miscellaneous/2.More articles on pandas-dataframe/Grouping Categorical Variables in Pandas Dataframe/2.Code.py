# importing pandas as pd
import pandas as pd

# Create the dataframe
df = pd.DataFrame({'A': ['a', 'b', 'c',
						'c', 'a', 'b'],
				'B': [0, 1, 1,
						0, 1, 0],
				'C':[7, 8, 9,
						5, 3, 6]})

# change tha datatype of
# column 'A' into category
# data type
df['A'] = df['A'].astype('category')

# initial state
print(df)

# calculating mean with
# all combinations of A and B
print(df.groupby(['A','B']).mean().reset_index())
