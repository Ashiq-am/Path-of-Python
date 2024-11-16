# make a series
new_column = df.groupby('Grade').Marks.transform('mean')

# view new series
print(new_column)

# add column in dataframe
df["Marks Mean"] = df.groupby('Grade').Marks.transform('mean')

# view modified dataframe
print(df)
