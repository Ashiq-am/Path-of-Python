# Filter top scoring students
df = df[df['Marks'] >= 75]

# Remove age row
df = df.drop(['Age'], axis=1)

# Display data
df
