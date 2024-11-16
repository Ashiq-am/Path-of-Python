import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [7, 8]})

# Changing columns name with index number
mapping = {df.columns[0]: 'new0', df.columns[1]: 'new1'}
su = df.rename(columns=mapping)

# Display
display(su)
