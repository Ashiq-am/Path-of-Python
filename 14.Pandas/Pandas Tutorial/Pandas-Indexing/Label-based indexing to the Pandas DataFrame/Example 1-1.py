# Use concept of fancy indexing to make new
# column 'Value' in data frame
# with help of dataframe.lookup() function
df['Value'] = df.lookup(df.index, df['Alpha'])

# Modified Data frame
df
