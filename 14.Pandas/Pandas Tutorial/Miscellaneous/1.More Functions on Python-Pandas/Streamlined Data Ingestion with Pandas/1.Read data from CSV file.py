# Import the Pandas library
import pandas

# Load data from Comma separated file
# Use method - read_csv(filepath)
# Parameter - the path/URL of the CSV/TXT file
dfIndianMetros = pandas.read_csv("gfg_indianmetros.csv")

# print the dataframe object
print(dfIndianMetros)
