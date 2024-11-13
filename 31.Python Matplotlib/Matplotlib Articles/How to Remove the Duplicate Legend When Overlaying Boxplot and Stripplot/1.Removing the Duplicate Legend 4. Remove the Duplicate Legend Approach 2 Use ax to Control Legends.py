# Create a figure and axis object
fig, ax = plt.subplots(figsize=(8, 6))

# Create the boxplot
sns.boxplot(x="day", y="total_bill", data=tips, hue="sex", palette="coolwarm", ax=ax)

# Overlay the stripplot
sns.stripplot(x="day", y="total_bill", data=tips, hue="sex",
              dodge=True, palette="coolwarm", linewidth=1, edgecolor='gray', ax=ax)

# Remove duplicate legends
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:2], labels[:2])

plt.show()
