# boxplot with showmeans
plt.figure(figsize=(10, 8))
sns.boxplot(x='survived',
			y='age',
			data=df,
			showmeans=True) # notice the change
plt.ylabel("Age", size=14)
plt.xlabel("Survived", size=14)
plt.title("Titanic Dataset", size=18)
