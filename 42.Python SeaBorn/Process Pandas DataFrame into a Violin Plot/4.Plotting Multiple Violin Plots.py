# Grouping violin plots by multiple categories
sns.violinplot(x='Group', y='Values', hue='Subgroup', data=df)
plt.show()
