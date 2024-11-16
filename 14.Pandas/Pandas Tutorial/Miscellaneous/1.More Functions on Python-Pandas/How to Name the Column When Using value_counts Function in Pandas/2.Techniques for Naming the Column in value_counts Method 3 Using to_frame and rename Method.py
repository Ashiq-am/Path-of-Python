import pandas as pd

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo']})

# Using value_counts, to_frame, and renaming the column
value_counts = df['A'].value_counts().to_frame('Count').reset_index().rename(columns={'index': 'Value'})
print(value_counts)
