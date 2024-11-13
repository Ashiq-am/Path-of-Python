# Customizing colors
sns.boxplot(x="day", y="total_bill", data=tips, palette="Set2")
sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")
plt.show()
