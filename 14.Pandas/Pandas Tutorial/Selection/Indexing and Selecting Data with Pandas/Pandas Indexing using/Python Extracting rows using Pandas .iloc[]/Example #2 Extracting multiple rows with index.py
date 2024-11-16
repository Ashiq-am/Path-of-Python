''''''

'''In this example, multiple rows are extracted first by passing a list and then by passing 
integers to extract rows between that range. After that, both the values are compared.'''


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

# retrieving rows by loc method
row1 = data.iloc[[4, 5, 6, 7]]

# retrieving rows by loc method
row2 = data.iloc[4:8]

# comparing values
row1 == row2
