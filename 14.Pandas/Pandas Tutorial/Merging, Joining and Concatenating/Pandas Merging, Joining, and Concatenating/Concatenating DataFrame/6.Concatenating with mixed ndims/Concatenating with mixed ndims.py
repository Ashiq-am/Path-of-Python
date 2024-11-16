'''
'''
'''User can concatenate a mix of Series and DataFrame. The Series will be transformed to DataFrame with 
the column name as the name of the Series.'''

# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=[0, 1, 2, 3])

# creating a series
s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')

print(df, "\n\n", s1)