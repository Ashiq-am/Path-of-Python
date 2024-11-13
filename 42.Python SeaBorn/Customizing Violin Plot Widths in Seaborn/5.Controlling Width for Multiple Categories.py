sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True, width=0.8)
plt.show()
