# You can simply change into horizontal
# boxplots by swapping x and y axes.
# Illustrating box plot
sns.boxplot(x="Dessert", y="Votes", data=data_df)

# Illustrating strip plot
sns.stripplot(x="Dessert", y="Votes", color='black',
			alpha=0.3, data=data_df)
