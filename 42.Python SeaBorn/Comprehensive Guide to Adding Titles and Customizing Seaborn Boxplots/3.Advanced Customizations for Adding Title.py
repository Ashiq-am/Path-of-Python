# Sample data with an additional category
data = pd.DataFrame({
    'Score': [33, 24, 29, 25, 30, 29, 34, 37],
    'Player': ['X', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y'],
    'Category': ['A', 'A', 'B', 'B', 'A', 'A', 'B', 'B']
})

# Create a boxplot with a legend
ax = sns.boxplot(data=data, x='Player', y='Score', hue='Category')
ax.set_title('Scores by Player and Category')
plt.legend(title='Category')
plt.show()
