# Python program to illustrate
# creating a data frame using CSV files

# import pandas module
import pandas as pd
# import csv module
import csv

with open("CardioGoodFitness.csv") as csv_file:
	# read the csv file
	csv_reader = csv.reader(csv_file)

	# now we can use this csv files into the pandas
	df = pd.DataFrame([csv_reader], index = None)

# iterating values of first column
for val in list(df[1]):
	print(val)
