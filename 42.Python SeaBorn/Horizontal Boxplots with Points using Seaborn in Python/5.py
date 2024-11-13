# It will create the data points inside the boxplot
# Illustrating box plot
sns.boxplot(y="Dessert", x="Votes", data=data_df)

# Illustrating strip plot
sns.stripplot(y="Dessert", x="Votes", color='black',
			alpha=0.3, data=data_df)
