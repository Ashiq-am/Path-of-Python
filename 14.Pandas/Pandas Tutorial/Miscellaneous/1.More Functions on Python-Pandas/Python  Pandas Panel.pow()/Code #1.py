# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks', 'real'],
                    'b': [111, 123, 425, 1333]})

df2 = pd.DataFrame({'a': ['I', 'am', 'dataframe', 'two'],
                    'b': [2, 3, 2, 2]})

data = {'item1': df1, 'item2': df2}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')
print("panel['b'] is - \n\n", panel['b'])

print("\nExponential power of panel['b']['item1'] with df2['b'] using pow() method - \n")
print("\n", panel['b']['item1'].pow(df2['b'], axis=0))
