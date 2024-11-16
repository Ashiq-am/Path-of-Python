# Create the boxplot sorted by median
plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Values', data=df)
plt.title('Boxplot Sorted by Median Values')
plt.show()
