# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks', 'for', 'real'],
                    'b': [11, 1.025, 333, 114.48, 1333]})

# Create a 5 * 5 dataframe
df2 = pd.DataFrame(np.random.rand(10, 2), columns=['a', 'b'])

data = {'item1': df1, 'item2': df2}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')
print("panel['b'] is - \n\n", panel['b'], '\n')

print("\nShape of Panel is - ", panel['b'].shape)
