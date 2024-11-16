# importing pandas module
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': ['Geeks', 'For', 'geeks', 'for', 'real'],
					'b': [11, 1.025, 333, 114.48, 1333]})

data = {'item1':df1, 'item2':df1}

# creating Panel
panel = pd.Panel.from_dict(data, orient ='minor')
print("panel['b'] is - \n\n", panel['b'], '\n')

# Create a 5 * 5 dataframe
df2 = pd.DataFrame(np.random.rand(5, 2), columns =['item1', 'item2'])
print("Newly create dataframe with random values is - \n\n", df2)

print("\nDividing panel['b'] with df2 using div() method - \n")
print(panel['b'].div(df2, axis = 0))
