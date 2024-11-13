# Create a boxplot and set the title using the set_title() method
ax = sns.boxplot(data=data, x='Player', y='Score')
ax.set_title('Scores by Player')
plt.show()
