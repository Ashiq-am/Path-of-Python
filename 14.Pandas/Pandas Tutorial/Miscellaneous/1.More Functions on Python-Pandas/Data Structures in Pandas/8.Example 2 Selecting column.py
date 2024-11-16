# Importing pandas as pd
from pandas import DataFrame

# Creating a data frame
Data = {'Name': ['Mohe', 'Shyni', 'Parul', 'Sam'],
        'ID': [12, 43, 54, 32],
        'Place': ['Delhi', 'Kochi', 'Pune', 'Patna']
        }

df = DataFrame(Data, columns=['Name', 'ID', 'Place'])

# Print original data frame
print("Original data frame:")
display(df)

print("Selected column: ")
display(df[['Name', 'ID']])
