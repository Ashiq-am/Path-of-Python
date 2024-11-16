"""DataFrame.loc[] method is used to retrieve rows from Pandas
DataFrame.Rows can also be selected by passing integer location to
an iloc[] function."""



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col="Name")

# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)