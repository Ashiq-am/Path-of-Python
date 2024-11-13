import matplotlib.pyplot as plt

# the slices are ordered and
# plotted counter-clockwise:
continents = ['Asia', 'Europe', 'North America',
			'South America','Australia',
			'Africa','Antarctica']

area = [25, 20, 15, 10,15,10,5]
explode = (0.1, 0, 0.1, 0,0.1,0.1,0.1)

plt.pie(area, explode = explode, labels = continents,
		autopct = '%1.1f%%',startangle = 0,
		wedgeprops = {"edgecolor" : "black",
					'linewidth' : 2,
					'antialiased': True})

# Equal aspect ratio ensures
# that pie is drawn as a circle.
plt.axis('equal')

plt.show()
