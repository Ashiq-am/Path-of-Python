# Create a sample DataFrame with multiple lines
df = pd.DataFrame({
    'day': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'store': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'sales': [3, 3, 5, 4, 7, 6, 8, 9, 12, 13]
})

# Create a line plot with multiple colors
sns.lineplot(data=df, x='day', y='sales', hue='store', palette=['red', 'blue'])
