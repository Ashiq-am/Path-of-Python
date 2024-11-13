import matplotlib.pyplot as plt

# the slices are ordered and plotted counter-clockwise:
sales = ['Product A', 'Product B',
		'Product C', 'Product D']

profit = [20, 30, 25, 20]
explode = (0.1, 0, 0.1, 0)

plt.pie(profit, explode = explode, labels = sales,
		autopct = '%1.1f%%',shadow = True,
		startangle = 90,
		wedgeprops = {"edgecolor":"black",
					'linewidth': 2,
					'antialiased': True})

# Equal aspect ratio ensures
# that pie is drawn as a circle.
plt.axis('equal')

plt.show()
