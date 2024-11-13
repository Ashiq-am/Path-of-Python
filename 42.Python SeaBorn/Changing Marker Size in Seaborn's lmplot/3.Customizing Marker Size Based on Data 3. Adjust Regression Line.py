sns.lmplot(x="total_bill", y="tip", data=tips, scatter_kws={"s": 150}, line_kws={"color": "blue", "lw": 2})
plt.show()
