# Importing pandas as pd
from pandas import DataFrame

# Creating a data frame
Data = {'Name': ['Mohe', 'Shyni', 'Parul', 'Sam'],
        'ID': [12, 43, 54, 32],
        'Place': ['Delhi', 'Kochi', 'Pune', 'Patna']
        }

df = DataFrame(Data, columns=['Name', 'ID', 'Place'])

# Print original data frame
print("Original data frame:\n")
display(df)

# Selecting the product of Electronic Type
select_prod = df.loc[df['Name'] == 'Mohe']

print("\n")

# Print selected rows based on the condition
print("Selecting rows:\n")
display(select_prod)
