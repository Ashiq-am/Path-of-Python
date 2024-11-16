# import pandas and numpy library
import pandas as pd
import numpy as np

# List of Tuples
matrix = [(1, 2, 3),
		(4, 5, 6),
		(7, 8, 9)
		]

# Create a DataFrame object
df = pd.DataFrame(matrix, columns = list('xyz'),
				index = list('abc'))

# Apply function numpy.square() to lambda
# to find the squares of the values of
# column whose column name is 'z'
new_df = df.apply(lambda x: np.square(x) if x.name == 'z' else x)

# Output
new_df
