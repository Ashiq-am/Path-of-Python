# Create a boxplot and set the title using the set() method
sns.boxplot(data=data, x='Player', y='Score').set(title='Scores by Player')
plt.show()
