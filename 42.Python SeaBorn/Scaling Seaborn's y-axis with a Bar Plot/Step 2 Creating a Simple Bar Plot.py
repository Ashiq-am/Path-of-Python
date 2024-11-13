# Sample data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 15, 25]}

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Create a bar plot
sns.barplot(x='Category', y='Values', data=df)
plt.show()
