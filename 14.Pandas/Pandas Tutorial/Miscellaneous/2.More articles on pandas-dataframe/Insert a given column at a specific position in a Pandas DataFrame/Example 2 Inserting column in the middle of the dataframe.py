# Importing pandas library
import pandas as pd

# dictionary
values = {'col2': [6, 7, 8,
				9, 10],
		'col3': [11, 12, 13,
				14, 15]}

# Creating dataframe
df = pd.DataFrame(values)

# New column to be added
new_col = [1, 2, 3, 4, 5]

# Inserting the column at the
# middle of the DataFrame
df.insert(loc = 1,
		column = 'col1',
		value = new_col)
# show the dataframe
df
