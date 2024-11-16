''''''
'''In order to join singly indexed dataframe with multi-indexed dataframe, the level will match on 
the name of the index of the singly-indexed frame against a level name of the multi-indexed frame.'''

# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav'],
         'Age': [27, 24, 22]}

# Define a dictionary containing employee data
data2 = {'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kanpur'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=pd.Index(['K0', 'K1', 'K2'], name='key'))

index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),
                                   ('K2', 'Y2'), ('K2', 'Y3')],
                                  names=['key', 'Y'])

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=index)

print(df, "\n\n", df1)