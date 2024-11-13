# Create the plot
ax = sns.barplot(x="day", y="proportion", hue="sex", data=grouped_data)

# Add percentage labels on bars
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width()/2, height + 0.01, f'{height:.2%}', ha="center")

plt.show()
