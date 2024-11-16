import pandas as pd

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo']})

# Using value_counts, reset_index, and rename
value_counts = df['A'].value_counts().reset_index().rename(columns={'index': 'Value', 'A': 'Count'})
print(value_counts)
