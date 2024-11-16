# Renaming our index column as 'new_index'
df.rename(columns = {'index':'new_index'},
		inplace = True)

# show the dataframe
df
