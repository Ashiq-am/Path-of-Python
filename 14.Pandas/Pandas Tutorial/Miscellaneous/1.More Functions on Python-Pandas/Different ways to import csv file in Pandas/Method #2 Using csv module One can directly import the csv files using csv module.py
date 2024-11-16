# import the module csv
import csv
import pandas as pd

# open the csv file
with open(r"C:\Users\Admin\Downloads\nba.csv") as csv_file:
    # read the csv file
    csv_reader = csv.reader(csv_file, delimiter=',')

    # now we can use this csv files into the pandas
    df = pd.DataFrame([csv_reader], index=None)
    df.head()

# iterating values of first column
for val in list(df[1]):
    print(val)
