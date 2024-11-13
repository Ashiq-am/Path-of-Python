# to plot a boxplot of
# age vs survived feature
plt.figure(figsize=(10, 8))
sns.boxplot(x='survived',
			y='age',
			data=df)
plt.ylabel("Age", size=14)
plt.xlabel("Survived", size=14)
plt.title("Titanic Dataset", size=18)
