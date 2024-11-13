# Filter out the blank rows
# from 'Name' column of df
df = df.filter(df.Name != '')

# Examine df
df.show()
