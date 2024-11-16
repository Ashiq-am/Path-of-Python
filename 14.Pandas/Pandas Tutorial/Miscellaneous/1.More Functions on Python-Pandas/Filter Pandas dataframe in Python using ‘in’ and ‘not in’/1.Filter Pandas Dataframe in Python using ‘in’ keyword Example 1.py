import pandas as pd

# Create a DataFrame with some sample data
df = pd.DataFrame({"A": [1, 2, 3, 4],
				"B": [5, 6, 7, 8]})

# Filter the DataFrame to include only rows
# where column "A" has a value of 1 or 2
df = df.query("A in [1, 2]")

# Print the resulting DataFrame
print(df)
