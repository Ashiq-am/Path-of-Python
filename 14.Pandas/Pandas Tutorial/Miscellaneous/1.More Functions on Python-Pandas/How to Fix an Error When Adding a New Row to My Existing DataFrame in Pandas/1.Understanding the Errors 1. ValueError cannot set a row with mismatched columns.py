import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'team': ['A', 'B', 'C'],
    'points': [18, 22, 19],
    'assists': [5, 7, 7]
})

# Define a new row with mismatched columns
new_row = ['D', 30]

# Attempt to add the new row
df.loc[len(df)] = new_row
