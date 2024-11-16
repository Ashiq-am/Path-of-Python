# import all required library
import xlrd
import csv
import pandas as pd

# open workbook by sheet index,
# optional - sheet_by_index()
sheet = xlrd.open_workbook("Test.xlsx").sheet_by_index(0)

# writer object is created
col = csv.writer(open("T.csv",
					'w',
					newline=""))

# writing the data into csv file
for row in range(sheet.nrows):
	# row by row write
	# operation is perform
	col.writerow(sheet.row_values(row))

# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv("T.csv"))

# show the dataframe
df
