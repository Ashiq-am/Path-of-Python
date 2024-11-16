# Import the Pandas library
import pandas

# Load data from an Excel file
# Use method - read_excel(filepath)
# Method parameter - The file location(URL/path) and name
dfBakery = pandas.read_excel("gfg_bakery.xlsx")

# print the dataframe object
print(dfBakery)
