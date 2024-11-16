# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks', 'real'],
                    'b': [-11, +1.025, -114.48, 1333]})

df2 = pd.DataFrame({'a': ['I', 'am', 'dataframe', 'two'],
                    'b': [100, 100, 100, 100]})

data = {'item1': df1, 'item2': df2}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')
print("panel['b'] is - \n\n", panel['b'])

print("\nAdding panel['b'] with df2['b'] using add() method - \n")
print("\n", panel['b'].add(df2['b'], axis=0))
