# Create a new column combining two categorical variables
tips["day_time"] = tips["day"].astype(str) + " - " + tips["time"].astype(str)

# Create a histogram with multiple hue columns
sns.histplot(data=tips, x="total_bill", hue="day_time", multiple="dodge", shrink=0.8)
plt.show()
