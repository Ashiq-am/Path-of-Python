# Seasonal plot
plt.figure(figsize=(7, 5))
sns.lineplot(x=data.index.month, y=data['Sunspots'], ci=None)
plt.xlabel('Month')
plt.ylabel('Number of Sunspots')
plt.title('Seasonal Plot')
plt.xticks(range(1, 13), labels=[
		'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
plt.show()
