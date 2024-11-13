# Customize the violin plot with a palette and additional inner plot
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True,
               palette="Set2", inner="quartile", scale="width")
plt.title("Customized Split Violin Plot with Quartiles")
plt.show()
