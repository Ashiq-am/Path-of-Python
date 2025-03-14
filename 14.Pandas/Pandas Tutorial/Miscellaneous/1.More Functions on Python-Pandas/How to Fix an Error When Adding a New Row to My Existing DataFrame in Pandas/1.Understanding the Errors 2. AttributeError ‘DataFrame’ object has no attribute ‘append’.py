import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'team': ['A', 'B', 'C'],
    'points': [18, 22, 19]
})

# Define a new row
new_row = {'team': 'D', 'points': 30}

# Attempt to append the new row
df = df.append(new_row, ignore_index=True)
