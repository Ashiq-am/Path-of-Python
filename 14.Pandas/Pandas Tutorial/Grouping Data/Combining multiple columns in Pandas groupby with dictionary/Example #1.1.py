# Creating the groupby dictionary
groupby_dict = {'Column 1.1':'Column 1',
				'Column 1.2':'Column 1',
				'Column 1.3':'Column 1',
				'Column 2.1':'Column 2',
				'Column 2.2':'Column 2' }

# Set the index of df as Column 'id'
df = df.set_index('id')

# Groupby the groupby_dict created above
df = df.groupby(groupby_dict, axis = 1).min()
print(df)
