# Adding hue for additional dimension
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips)
sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips, dodge=True)
plt.show()
