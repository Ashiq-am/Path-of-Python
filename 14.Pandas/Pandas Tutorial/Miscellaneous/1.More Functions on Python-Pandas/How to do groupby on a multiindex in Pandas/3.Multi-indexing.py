# using the pandas set_index().
# passing the name of the columns in the list.

df = df.set_index(['region' , 'state'])

# sort the data using sort_index()
df.sort_index()

print(df.head())
