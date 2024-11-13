# Create a violin plot split by 'sex'
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
plt.title("Violin Plot of Total Bill by Day (Split by Gender)")
plt.show()
