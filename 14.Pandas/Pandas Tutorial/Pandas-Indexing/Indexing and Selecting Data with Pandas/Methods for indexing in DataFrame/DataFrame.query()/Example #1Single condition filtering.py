"""

In this example, the data is filtered on the basis of single condition.
Before applying the query() method, the spaces in column names have been
replaced with ‘_’.

"""



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# replacing blank spaces with '_'
data.columns =[column.replace(" ", "_") for column in data.columns]

# filtering with query method
data.query('Senior_Management == True', inplace = True)

# display
data