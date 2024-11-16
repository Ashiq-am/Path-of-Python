# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks'],
                    'b': np.random.randn(3)})

data = {'item1': df1, 'item2': df1}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')
print(panel, "\n")
