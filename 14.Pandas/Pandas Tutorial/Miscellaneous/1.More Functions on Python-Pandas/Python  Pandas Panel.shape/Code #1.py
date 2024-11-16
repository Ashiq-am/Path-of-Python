# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks', 'for', 'real'],
                    'b': [11, 1.025, 333, 114.48, 1333]})

data = {'item1': df1, 'item2': df1}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')

print("panel['b'] is - \n\n", panel['b'], '\n')

print("\nSize of panel['b'] is - ", panel['b'].shape)
