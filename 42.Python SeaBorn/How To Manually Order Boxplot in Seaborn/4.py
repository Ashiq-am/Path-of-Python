# illustraing box plot with order
fx = sns.boxplot(x='day', y='total_bill', data=tips, order=[
				'Sun', 'Sat', 'Fri', 'Thur'], hue='sex', palette='Set2')
