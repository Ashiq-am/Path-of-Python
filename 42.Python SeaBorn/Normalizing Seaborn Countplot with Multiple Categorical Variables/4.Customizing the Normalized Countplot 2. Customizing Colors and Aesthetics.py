sns.set(style="whitegrid")
sns.barplot(x="day", y="proportion", hue="sex", data=grouped_data, palette="Set2")
plt.show()
