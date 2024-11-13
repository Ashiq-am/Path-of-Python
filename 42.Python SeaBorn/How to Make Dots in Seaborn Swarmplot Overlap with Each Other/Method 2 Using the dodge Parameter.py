# Create a swarmplot with dodge
sns.swarmplot(x='day', y='total_bill', hue='sex', data=tips, dodge=True)
plt.title('Swarmplot with Dodge')
plt.show()
