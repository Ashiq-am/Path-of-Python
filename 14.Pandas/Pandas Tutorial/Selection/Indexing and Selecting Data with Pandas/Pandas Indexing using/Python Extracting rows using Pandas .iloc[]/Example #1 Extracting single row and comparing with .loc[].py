''''''
'''In this example, same index number row is extracted by both .iloc[] and.loc[] method and compared.
Since the index column by default is numeric, hence the index label will also be integers.'''


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

# retrieving rows by loc method
row1 = data.loc[3]

# retrieving rows by iloc method
row2 = data.iloc[3]

# checking if values are equal
row1 == row2
