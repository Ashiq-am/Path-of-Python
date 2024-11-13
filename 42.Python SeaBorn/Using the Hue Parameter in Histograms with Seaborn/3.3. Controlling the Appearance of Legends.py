sns.histplot(data=tips, x="total_bill", hue="day", legend=False, multiple="dodge", shrink=0.8)
plt.show()
