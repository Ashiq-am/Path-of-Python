# importing pandas as pd
import pandas as pd

# Create the dataframe
# with categorical variable
df = pd.DataFrame({'A': ['a', 'b', 'c',
						'c', 'a', 'b'],
				'B': [0, 1, 1, 0, 1, 0]},
				dtype = "category")
# show the data types
df.dtypes
