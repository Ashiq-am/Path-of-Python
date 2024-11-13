sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips, scatter_kws={"s": 150})
plt.show()
