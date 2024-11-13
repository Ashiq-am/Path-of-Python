# import pandas with shortcut 'pd'
import pandas as pd

# read_csv function which is used to read the required CSV file
data = pd.read_csv('input.csv')

# display
print("Original 'input.csv' CSV Data: \n")
print(data)

# pop function which is used in removing or deleting columns from the CSV files
data.pop('year')

# display
print("\nCSV Data after deleting the column 'year':\n")
print(data)
