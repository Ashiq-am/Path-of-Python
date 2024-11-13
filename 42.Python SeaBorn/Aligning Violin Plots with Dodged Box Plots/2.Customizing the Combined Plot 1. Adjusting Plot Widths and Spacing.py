# Create a figure
plt.figure(figsize=(8, 6))

# Plot violin plot with reduced width
sns.violinplot(x="pclass", y="fare", hue="sex", data=df, split=True, inner=None, width=0.8)

# Plot box plot with reduced width and dodge for alignment
sns.boxplot(x="pclass", y="fare", hue="sex", data=df, dodge=True, width=0.3, showcaps=False, boxprops={'facecolor':'None'}, showfliers=False, whiskerprops={'linewidth':2})

plt.legend(loc='upper right')
plt.show()
