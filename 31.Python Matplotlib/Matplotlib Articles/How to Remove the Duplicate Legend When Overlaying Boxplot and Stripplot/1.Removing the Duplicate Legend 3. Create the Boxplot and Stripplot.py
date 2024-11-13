plt.figure(figsize=(8, 6))

# Create a boxplot
sns.boxplot(x="day", y="total_bill", data=tips, hue="sex", palette="coolwarm")

# Overlay a stripplot
sns.stripplot(x="day", y="total_bill", data=tips, hue="sex",
              dodge=True, palette="coolwarm", linewidth=1, edgecolor='gray')

plt.show()
