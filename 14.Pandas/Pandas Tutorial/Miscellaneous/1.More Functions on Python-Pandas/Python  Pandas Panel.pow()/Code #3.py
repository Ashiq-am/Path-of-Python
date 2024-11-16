# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks', 'for', 'real'],
                    'b': [2, 4, 6, 6, 10]})

df2 = pd.DataFrame({'a': ['I', 'am', 'DataFrame', 'number', 'two'],
                    'b': [10, 5, 3, 6, 7]})

data = {'item1': df1, 'item2': df2}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')

print("panel['b'] is - \n\n", panel['b'], '\n')

print("\nExponential power of panel['b']['item1'] with df2['b'] or panel['b']['item2'] using pow() method - \n")
print("\n", panel['b']['item1'].pow(df2['b'], axis=0))
