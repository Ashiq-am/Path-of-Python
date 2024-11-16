'''
'''

'''In the following example, Team column is checked for NULL values and a boolean series is returned by 
the isnull() method which stores True for ever NaN value and False for a Not null value.'''



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# creating bool series True for NaN values
bool_series = pd.isnull(data["Gender"])

# filtering data
# displayind data only with team = NaN
data[bool_series]
