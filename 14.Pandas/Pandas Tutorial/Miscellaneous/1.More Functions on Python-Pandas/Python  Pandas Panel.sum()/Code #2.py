# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks', 'for', 'real'],
                    'b': [33.0, -152.140, 3.0133, 114.48, 13.033]})

data = {'item1': df1, 'item2': df1}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')

print(panel['b'], '\n')

print("\n", panel['b'].sum(axis=1))
