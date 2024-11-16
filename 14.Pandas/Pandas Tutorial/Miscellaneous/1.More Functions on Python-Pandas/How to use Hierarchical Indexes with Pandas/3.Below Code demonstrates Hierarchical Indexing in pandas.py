# using the pandas set_index() function.
df_ind3 = df.set_index(['region', 'state', 'individuals'])

# we can sort the data by using sort_index()
df_ind3.sort_index()

print(df_ind3.head(10))
