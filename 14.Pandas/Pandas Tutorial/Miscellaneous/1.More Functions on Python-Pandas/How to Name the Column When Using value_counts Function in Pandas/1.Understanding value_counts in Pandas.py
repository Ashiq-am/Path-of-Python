import pandas as pd
data = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])

# Using value_counts
value_counts = data.value_counts()
print(value_counts)
