import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})

# Changing columns name with index number
su = df.rename(columns={df.columns[1]: 'new'})

# Display
display(su)
