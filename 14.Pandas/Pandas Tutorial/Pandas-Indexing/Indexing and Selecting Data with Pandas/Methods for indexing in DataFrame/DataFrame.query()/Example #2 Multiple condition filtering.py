# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# replacing blank spaces with '_'
data.columns =[column.replace(" ", "_") for column in data.columns]

# filtering with query method
data.query('Senior_Management == True and Gender =="Male" and Team =="Marketing" '
           'and First_Name =="Johnny"', inplace = True)

# display
data




"""
 In this example, dataframe has been filtered on multiple conditions. 
 Before applying 
 the query() method, the spaces in column names have been replaced with ‘_’.

"""
