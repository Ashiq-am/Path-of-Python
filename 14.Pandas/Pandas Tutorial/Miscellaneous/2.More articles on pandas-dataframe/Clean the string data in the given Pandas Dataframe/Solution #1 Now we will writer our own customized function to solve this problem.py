def Format_data(df):
	# iterate over all the rows
	for i in range(df.shape[0]):

		# reassign the values to the product column
		# we first strip the whitespaces using strip() function
		# then we capitalize the first letter using capitalize() function
		df.iat[i, 1]= df.iat[i, 1].strip().capitalize()

# Let's call the function
Format_data(df)

# Print the Dataframe
print(df)
