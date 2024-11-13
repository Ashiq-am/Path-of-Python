# customizing using meanprops
plt.figure(figsize=(10, 8))
sns.boxplot(x='survived',
			y='age',
			data=df,
			showmeans=True,
			meanprops={"marker": "+",
					"markeredgecolor": "black",
					"markersize": "10"})
plt.ylabel("Age", size=14)
plt.xlabel("Survived", size=14)
plt.title("Titanic Dataset", size=18)
