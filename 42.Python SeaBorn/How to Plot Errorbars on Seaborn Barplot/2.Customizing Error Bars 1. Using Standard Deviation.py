# Plot with custom confidence interval
sns.barplot(x="day", y="total_bill", data=tips, ci=85)

# Plot using standard deviation
sns.barplot(x="day", y="total_bill", data=tips, ci="sd")
