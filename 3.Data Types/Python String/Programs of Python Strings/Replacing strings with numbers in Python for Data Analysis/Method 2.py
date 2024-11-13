# import pandas library
import pandas as pd

# creating file handler for
# our example.csv file in
# read mode
file_handler = open("example.csv", "r")

# creating a Pandas DataFrame
# using read_csv function that
# reads from a csv file.
data = pd.read_csv(file_handler, sep = ",")

# closing the file handler
file_handler.close()

# traversing through Gender
# column of dataFrame and
# writing values where
# condition matches.
data.Gender[data.Gender == 'male'] = 1
data.Gender[data.Gender == 'female'] = 2
print(data)
