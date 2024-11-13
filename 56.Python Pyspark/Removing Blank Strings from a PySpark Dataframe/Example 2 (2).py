# filter out rows with blank strings
# in the "Name" and "Address" columns
df = df.filter((df.Name != '') & (df.Address != ''))

# examine the dataframe
df.show()
