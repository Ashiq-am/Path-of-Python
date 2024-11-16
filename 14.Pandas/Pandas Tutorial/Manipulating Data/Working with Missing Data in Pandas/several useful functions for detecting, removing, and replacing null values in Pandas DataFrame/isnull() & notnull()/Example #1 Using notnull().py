'''
'''

'''In the following example, Gender column is checked for NULL values and a boolean series is returned 
by the notnull() method which stores True for ever NON-NULL value and False for a null value.'''


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# creating bool series False for NaN values
bool_series = pd.notnull(data["Gender"])

# displayed data only with team = NaN
data[bool_series]
