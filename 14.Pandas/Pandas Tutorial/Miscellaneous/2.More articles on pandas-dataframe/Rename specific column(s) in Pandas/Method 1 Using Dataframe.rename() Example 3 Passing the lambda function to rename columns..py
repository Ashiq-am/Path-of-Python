# using the same modified dataframe
# df from Renaming Multiple Columns
# this adds ':' at the end
# of each column name
df = df.rename(columns = lambda x: x+':')

# printing the columns
print(df.columns)
