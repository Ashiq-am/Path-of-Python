# create 3rd grouped boxplot
sns.boxplot(x = data['day'],
			y = data['total_bill'],
			hue = data['size'],
			palette = 'husl')
