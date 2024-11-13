# Plot normalized countplot
sns.barplot(x="day", y="proportion", hue="sex", data=grouped_data)
plt.ylabel('Proportion')
plt.title('Normalized Countplot by Day and Sex')
plt.show()
