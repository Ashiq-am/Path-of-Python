# Adjust size
plt.figure(figsize=(8.3,6))

# Illustrate boxplot
sns.boxplot(y="Dessert", x="Votes", data=data_df)
