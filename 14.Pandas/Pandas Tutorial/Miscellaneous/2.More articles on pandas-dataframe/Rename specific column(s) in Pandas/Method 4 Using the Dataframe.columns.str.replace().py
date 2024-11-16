# printing the column
# names before renaming
print(df.columns)

# Replacing the space in column
# names by an underscore
df.columns = df.columns.str.replace(' ', '_')

# printing the column names
# after renaming
print(df.columns)
