# Creating another object using groupby
grouped2 = df.groupby('Score')

# the return type of the object 'grouped2' is
# pandas.core.groupby.generic.DataFrameGroupBy.

# Creating a dataframe from the object
# using get_group() dataframe of students
# with Score = 90
df_grouped2 = grouped2.get_group(90)

print(df_grouped2)
