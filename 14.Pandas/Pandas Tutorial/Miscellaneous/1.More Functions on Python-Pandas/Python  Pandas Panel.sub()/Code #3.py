# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks', 'for', 'real'],
                    'b': [11, 1.025, 333, 114.48, 1333]})

df2 = pd.DataFrame({'a': ['I', 'am', 'DataFrame', 'number', 'two'],
                    'b': [10, 10, 10, 110, 110]})

data = {'item1': df1, 'item2': df2}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')

print("panel['b'] is - \n\n", panel['b'], '\n')

print("\nSubtracting panel['b']['item1'] with df2['b'] or panel['b']['item2'] using sub() method - \n")
print("\n", panel['b']['item1'].sub(df2['b'], axis=0))
