# Sample data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 15, 25]}

df = pd.DataFrame(data)

# Create a bar plot with customizations
sns.barplot(x='Category', y='Values', data=df, palette='pastel')

# Customize the plot
plt.ylim(0, 30)
plt.title('Sample Bar Plot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.yticks([0, 10, 20, 30])

# Show the plot
plt.show()
