# import pandas library
import pandas as pd

# creating file handler for
# our example.csv file in
# read mode
file_handler = open("example.csv", "r")

# creating a Pandas DataFrame
# using read_csv function
# that reads from a csv file.
data = pd.read_csv(file_handler, sep = ",")

# closing the file handler
file_handler.close()

# creating a dict file
gender = {'male': 1,'female': 2}

# traversing through dataframe
# Gender column and writing
# values where key matches
data.Gender = [gender[item] for item in data.Gender]
print(data)
