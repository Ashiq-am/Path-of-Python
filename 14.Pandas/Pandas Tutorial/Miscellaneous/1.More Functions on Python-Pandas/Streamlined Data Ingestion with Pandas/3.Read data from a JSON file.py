# Import the Pandas library
import pandas

# Load data from a JSON file
# Use method - read_json(filepath)
# Method parameter - The file location(URL/path) and name
dfCodeCountry = pandas.read_json("gfg_codecountry.json")

# print the dataframe object
print(dfCodeCountry)
