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

# Apply function numpy.square() to
# square the values of two rows
# 'b' and 'c'
new_df = df.apply(lambda x: np.square(x) if x.name in ['b', 'c'] else x, axis = 1)

# Output
new_df
