''''''
'''In this example, .isdigit() method is applied on the Age column. Before doing any operations, 
null rows are removed using .dropna() to avoid errors.

Since the Age column is imported as Float dtype, it is first converted into string using .astype() method. 
After that the isdigit() is applied twice, first on the original series and after that ‘.’ 
is removed using str.replace() method to see the output after removing special characters.'''


# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace = True)

# converting dtype to string
data["Age"]= data["Age"].astype(str)

# removing '.'
data["Age new"]= data["Age"].str.replace(".", "")

# creating bool series with original column
data["bool_series1"]= data["Age"].str.isdigit()

# creating bool series with new column
data["bool_series2"]= data["Age new"].str.isdigit()

# display
data.head(10)
