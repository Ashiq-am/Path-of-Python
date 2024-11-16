# set the name of column axes
from pandas.tests.groupby.test_value_counts import df

df.rename_axis('Column_Index_name', axis = 'columns')

# Print the DataFrame
print(df)
