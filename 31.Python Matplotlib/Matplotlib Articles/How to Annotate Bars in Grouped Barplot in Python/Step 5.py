# code for annotated barplot
plt.figure(figsize=(8, 6))
splot = sns.barplot(x="class", y="avg_age", hue="sex",
					data=data_df, palette='Greens')

plt.ylabel("Average Age", size=14)
plt.xlabel("Ticket Class", size=14)
plt.title("Grouped Barplot with annotations", size=18)
for p in splot.patches:
	splot.annotate(format(round(p.get_height()), '.0f')+"Years",
				(p.get_x() + p.get_width() / 2., p.get_height()),
				ha='center', va='center',
				size=14,
				xytext=(0, -12),
				textcoords='offset points')
