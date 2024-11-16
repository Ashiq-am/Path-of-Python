import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})

# Changing columns name with index number
df.columns.values[0] = "b"
df.columns.values[1] = "a"

# Display
display(df)
