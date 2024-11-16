# Create a new column with Marks
# ranked in descending order
df['Mark_Rank'] = df['Marks'].rank(ascending = 0)

# Set index to newly created column
df = df.set_index('Mark_Rank')
print(df)
