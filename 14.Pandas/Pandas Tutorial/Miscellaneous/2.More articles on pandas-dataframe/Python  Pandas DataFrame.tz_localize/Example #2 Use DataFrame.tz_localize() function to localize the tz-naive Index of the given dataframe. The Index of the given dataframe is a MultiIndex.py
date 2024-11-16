# importing pandas as pd
import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Weight':[45, 88, 56, 15, 71],
				'Name':['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'],
				'Age':[14, 25, 55, 8, 21]})

# Create the MultiIndex
index_ = pd.MultiIndex.from_product([['Date'], pd.date_range('2010-10-09 08:45', periods = 5, freq ='H')],
		names =['Level 1', 'Level 2'])

# Set the index
df.index = index_

# Print the DataFrame
print(df)
