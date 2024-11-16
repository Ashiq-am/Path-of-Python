# Creating an object using groupby
grouped = df.groupby('Degree')

# the return type of the object 'grouped' is
# pandas.core.groupby.generic.DataFrameGroupBy.

# Creating a dataframe from the object using get_group().
# dataframe of students with Degree as MBA.
df_grouped = grouped.get_group('MBA')

print(df_grouped)
