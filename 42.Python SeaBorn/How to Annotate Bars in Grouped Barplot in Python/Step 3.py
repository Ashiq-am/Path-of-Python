# code to plot a simple grouped barplot
plt.figure(figsize=(8, 6))
sns.barplot(x="class", y="avg_age",
			hue="sex", data=data_df,
			palette='Greens')

plt.ylabel("Average Age", size=14)
plt.xlabel("Ticket Class", size=14)
plt.title("Simple Grouped Barplot", size=18)
