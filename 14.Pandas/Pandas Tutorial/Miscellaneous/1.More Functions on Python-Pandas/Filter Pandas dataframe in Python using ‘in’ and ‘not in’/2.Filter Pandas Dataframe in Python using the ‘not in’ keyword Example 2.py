# Filter the DataFrame to exclude rows
# where column "A" has a value of 1 or 2, and
# column "B" has a value of 6 or 7
df = df.query("not (A in [1, 2] and B in [6, 7])")

# Print the resulting DataFrame
print(df)
