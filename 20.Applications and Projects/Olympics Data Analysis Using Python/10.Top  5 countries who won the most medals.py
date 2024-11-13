print(goldMedals.region.value_counts().reset_index(name='Medal').head())

totalGoldMedals = goldMedals.region.value_counts()
.reset_index(name='Medal').head(5)
g = sns.catplot(x="index", y="Medal", data=totalGoldMedals,
				height=6, kind="bar", palette="muted")
g.despine(left=True)
g.set_xlabels("Top 5 countries")
g.set_ylabels("Number of Medals")
plt.title('Medals per Country')
plt.show()
