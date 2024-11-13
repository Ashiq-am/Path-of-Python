# code for annotated grouped barplot
plt.figure(figsize=(8, 6))
splot = sns.barplot(x="class", y="avg_age", hue="sex",
                    data=data_df, palette='Greens')

for p in splot.patches:
    splot.annotate(format(p.get_height()),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center',
                   xytext=(0, 9),
                   textcoords='offset points')

plt.ylabel("Average Age", size=14)
plt.xlabel("Ticket Class", size=14)
plt.title("Grouped Barplot with annotations", size=18)
