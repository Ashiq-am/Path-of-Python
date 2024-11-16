# import pandas library
import pandas as pd

# create a dataframe
df = pd.DataFrame( {'a': ['A', 'A', 'B',
						'B', 'B', 'C',
						'C', 'D'],
					'b': [1, 2, 5,
						3, 5, 4,
						8, 6]}
				)
# convert values of each group
# into a list
groups = df.groupby('a').agg(lambda
							x: list(x))

print(groups)
