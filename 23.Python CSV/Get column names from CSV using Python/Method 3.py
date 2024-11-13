# importing the pandas library
import pandas as pd

# reading the csv file using read_csv
# storing the data frame in variable called df
df = pd.read_csv('data.csv')

# creating a list of column names by
# calling the .columns
list_of_column_names = list(df.columns)

# displaying the list of column names
print('List of column names : ',
	list_of_column_names)
