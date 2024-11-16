import pandas as pd

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo']})

# Using value_counts and renaming the resulting Series
value_counts = df['A'].value_counts().rename('Count')
print(value_counts)
