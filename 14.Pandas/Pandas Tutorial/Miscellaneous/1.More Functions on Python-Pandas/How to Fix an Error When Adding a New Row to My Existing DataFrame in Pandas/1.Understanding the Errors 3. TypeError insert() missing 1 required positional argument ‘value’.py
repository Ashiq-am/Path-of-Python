import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'team': ['A', 'B', 'C'],
    'points': [18, 22, 19]
})

# Attempt to insert a new row
df.insert(len(df), ['D', 30])
