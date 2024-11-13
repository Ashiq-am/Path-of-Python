# Create a swarmplot with smaller dots
sns.swarmplot(x='day', y='total_bill', data=tips, size=3)
plt.title('Swarmplot with Smaller Dots')
plt.show()
