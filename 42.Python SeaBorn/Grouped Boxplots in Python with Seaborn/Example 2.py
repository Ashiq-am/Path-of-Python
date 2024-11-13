# create another grouped boxplot
sns.boxplot(x = data['day'],
			y = data['total_bill'],
			hue = data['smoker'],
			palette = 'Set2')
