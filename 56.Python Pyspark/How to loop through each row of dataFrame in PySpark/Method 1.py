# retrieving all the elements
# of the dataframe using collect()
# Storing in the variable
data_collect = df.collect()

# looping thorough each row of the dataframe
for row in data_collect:
	# while looping through each
	# row printing the data of Id, Name and City
	print(row["Id"],row["Name"]," ",row["City"])
