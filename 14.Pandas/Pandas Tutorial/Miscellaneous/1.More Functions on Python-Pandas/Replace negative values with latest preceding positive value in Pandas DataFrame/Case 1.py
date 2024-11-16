import pandas as pd


# creating a pandas dataframe
df = pd.DataFrame([[8, -2, 0, 3, 51, 2],
				[6, -2, -5, -7, 0, -1],
				[-1, -12, -5, 4, 5, 3]])
print("Original DataFrame : \n")
print(df)

# declaring a pre defined value
prec_val = -999

# iterate over columns
for i in range(df.shape[1]):

	# resetting value over each column
	prec_val = -999

	# iterate over rows
	for j in range(df.shape[0]):

		# accessing the cell value
		cell = df.at[j, i]

		# check if cell value is negative
		if(cell < 0):

			# check if prec_val is not default
			# set value
			if(prec_val != -999):

				# replace the cell value
				df.at[j, i] = prec_val
		else:

			# store the latest value in variable
			prec_val = df.at[j, i]

print("Modified DataFrame : ")
print(df)
