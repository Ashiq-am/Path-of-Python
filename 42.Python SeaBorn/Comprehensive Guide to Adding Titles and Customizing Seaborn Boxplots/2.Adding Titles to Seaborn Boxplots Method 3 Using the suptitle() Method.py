# Create a boxplot and set the title using the suptitle() method
fig, ax = plt.subplots()
sns.boxplot(data=data, x='Player', y='Score', ax=ax)
fig.suptitle('Scores by Player')
plt.show()
