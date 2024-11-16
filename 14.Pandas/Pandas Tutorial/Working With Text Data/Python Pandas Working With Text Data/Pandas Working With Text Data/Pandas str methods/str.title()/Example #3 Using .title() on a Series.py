""""""
'''In this example, .title() function is being called by the Team column and hence, all the values in 
the into column will be converted in to Camel case. Since the values in the Team column were already in 
camel case, it has been converted to Upper case before and then again to camel case in order to verify 
the functionality of .title() method.'''


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# converting and overwriting values in column
data["Team"]= data["Team"].str.upper().str.title()

# display
data
