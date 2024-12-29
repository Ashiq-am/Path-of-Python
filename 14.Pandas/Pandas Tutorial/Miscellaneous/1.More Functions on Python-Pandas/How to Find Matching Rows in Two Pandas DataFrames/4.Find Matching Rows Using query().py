import pandas as pd

# Create the first DataFrame: df1
df1 = pd.DataFrame({
    'BookID': [101, 102, 103],
    'Title': ['To Kill a Mockingbird', '1984', 'The Great Gatsby']
})

# Create the second DataFrame: df2
df2 = pd.DataFrame({
    'BookID': [103, 105, 107],
    'Genre': ['Classic', 'Romance', 'Science Fiction']
})

# Find rows in df1 where 'BookID' matches with 'BookID' in df2 using query()
# Convert df2['BookID'] to a list to avoid the ValueError
result = df1.query("BookID in @df2.BookID").merge(
    df2.query("BookID in @df1.BookID"),
    on="BookID",
    how="inner"
)

# Print the result
print(result)