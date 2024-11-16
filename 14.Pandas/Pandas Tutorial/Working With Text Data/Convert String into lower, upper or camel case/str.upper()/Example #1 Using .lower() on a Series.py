''''''
'''In this example, .lower() function is being called by the First Name column and hence, all the values 
in the First name column will be converted in to lower case.'''


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# converting and overwriting values in column
data["First Name"]= data["First Name"].str.lower()

# display
data
