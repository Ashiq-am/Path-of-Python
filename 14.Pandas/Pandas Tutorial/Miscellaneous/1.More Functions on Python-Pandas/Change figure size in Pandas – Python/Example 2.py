# import the pandas module
import pandas as pd

# Creating a pandas dataframe
df = pd.DataFrame({'names': ['A', 'B', 'C', 'D'], 'val': [10, 45, 30, 20]})

# creates a bar graph of size 15 inches wide and 10 inches high
df.plot.bar(x='names', y='val', rot=0, figsize=(15, 10))
