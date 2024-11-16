# creating a list of dataframe columns
from pandas.tests.test_downstream import df

columns = list(df)

for i in columns:

	# printing the third element of the column
	print (df[i][2])
