# Grouped Countplot/Barplot
# Count of passengers who survived
# or didn't of each gender
sns.catplot(x='sex', hue='survived',
			kind='count', data=data)

plt.xlabel("Gender")
plt.ylabel("Count")
