# creating a list of dataframe columns
from pip._vendor.pyparsing import col

clmn = list(col)

for i in clmn:
	# printing a third element of column
	print(col[i][2])
