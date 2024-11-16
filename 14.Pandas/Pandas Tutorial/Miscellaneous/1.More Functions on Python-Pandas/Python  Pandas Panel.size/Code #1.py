# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks', 'for', 'real'],
                    'b': [11, 1.025, 333, 114.48, 1333]})

print("df1 is - \n\n", df1)

# Create a 5 * 5 dataframe
df2 = pd.DataFrame(np.random.rand(10, 2), columns=['a', 'b'])
print("df2 is - \n\n", df2)
