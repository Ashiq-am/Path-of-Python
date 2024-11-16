# Define the bin edges
bins = [0, 1, 2, 3, 4, 5, 6]

# Categorize the 'Values' column into bins
df['Categories'] = pd.cut(df['Values'], bins)

print(df)
