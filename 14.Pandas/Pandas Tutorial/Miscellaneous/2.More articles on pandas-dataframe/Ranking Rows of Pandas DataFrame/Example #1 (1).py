# Create a column Rating_Rank which contains
# the rank of each movie based on rating
df['Rating_Rank'] = df['Rating'].rank(ascending = 1)

# Set the index to newly created column, Rating_Rank
df = df.set_index('Rating_Rank')
print(df)
