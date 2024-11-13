# Create a basic violin plot
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Basic Violin Plot of Total Bill by Day")
plt.show()
