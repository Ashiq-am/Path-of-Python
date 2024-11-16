# Function to insert row in the dataframe
def Insert_row_(row_number, df, row_value):
	# Slice the upper half of the dataframe
	df1 = df[0:row_number]

	# Store the result of lower half of the dataframe
	df2 = df[row_number:]

	# Inser the row in the upper half dataframe
	df1.loc[row_number]=row_value

	# Concat the two dataframes
	df_result = pd.concat([df1, df2])

	# Reassign the index labels
	df_result.index = [*range(df_result.shape[0])]

	# Return the updated dataframe
	return df_result

# Let's create a row which we want to insert
row_number = 2
row_value = ['11/2/2011', 'Wrestling', 12000]

if row_number > df.index.max()+1:
	print("Invalid row_number")
else:

	# Let's call the function and insert the row
	# at the second position
	df = Insert_row_(2, df, row_value)

	# Print the updated dataframe
	print(df)
