# Sample data
data = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])

# Using value_counts and pipe
df = (data.value_counts()
      .reset_index()
      .pipe(lambda x: x.rename(columns={'index': 'Fruit', 0: 'Count'})))

print(df)
