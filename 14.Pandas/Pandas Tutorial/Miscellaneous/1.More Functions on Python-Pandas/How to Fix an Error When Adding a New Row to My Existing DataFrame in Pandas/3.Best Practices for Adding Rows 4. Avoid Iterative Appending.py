import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'team': ['A', 'B', 'C'],
    'points': [18, 22, 19]
})

# Collect new rows in a list
new_rows = [
    {'team': 'D', 'points': 30},
    {'team': 'E', 'points': 25}
]

# Append the new rows using concat
df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
print(df)
