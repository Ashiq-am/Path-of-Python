data = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
value_counts = data.value_counts()

# Convert to DataFrame and rename columns using assign
df = value_counts.reset_index().assign(Fruit=lambda x: x['index'], Count=lambda x: x[0]).drop(columns=['index', 0])
print(df)
