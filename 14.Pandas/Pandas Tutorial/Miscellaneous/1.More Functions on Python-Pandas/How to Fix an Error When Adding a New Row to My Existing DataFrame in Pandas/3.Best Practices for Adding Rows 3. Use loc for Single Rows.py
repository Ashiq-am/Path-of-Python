import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'team': ['A', 'B', 'C'],
    'points': [18, 22, 19]
})

# Define a new row
new_row = {'team': 'D', 'points': 30}

# Append the new row using loc
df.loc[len(df)] = new_row
print(df)
