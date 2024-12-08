import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [10, 20, 30, 40]
})

# Create a new column by referencing the next row using iloc
df['A_next_iloc'] = pd.concat([df['A'].iloc[1:].reset_index(drop=True), pd.Series([None])], ignore_index=True)

# Print the resulting DataFrame
print(df)