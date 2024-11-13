# Create a figure
plt.figure(figsize=(8, 6))

# Custom color palette for sexes
palette = {"male": "skyblue", "female": "lightpink"}

# Plot violin plot with custom palette
sns.violinplot(x="pclass", y="fare", hue="sex", data=df, split=True, inner=None, palette=palette, width=0.8)

# Plot box plot with dodge, transparent boxes, and custom palette
sns.boxplot(x="pclass", y="fare", hue="sex", data=df, dodge=True, width=0.3, showcaps=False, boxprops={'facecolor':'None'}, showfliers=False, whiskerprops={'linewidth':2}, palette=palette)

plt.legend(loc='upper right')
plt.show()
