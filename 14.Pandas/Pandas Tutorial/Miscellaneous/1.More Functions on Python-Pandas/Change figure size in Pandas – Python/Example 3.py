# import the pandas module
import pandas as pd

# Creating a pandas dataframe with index
df = pd.DataFrame({'value': [3.330, 4.87, 5.97]},
				index=['Item 1', 'Item 2', 'Item 3'])

df.plot.pie(y='value', figsize=(5, 5))
