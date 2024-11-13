# Plotting horizontally
sns.catplot(y='sex', hue='survived',
			kind='count', data=data)

plt.xlabel("Count")
plt.ylabel("Gender")
