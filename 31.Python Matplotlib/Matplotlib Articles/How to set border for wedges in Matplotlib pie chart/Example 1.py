import matplotlib.pyplot as plt

years = [2016, 2017, 2018, 2019, 2020]
profit = [15, 19, 35, 14, 17]

# Plotting the pie chart
plt.pie(profit, labels = years, autopct = '%1.1f%%',
		startangle = 90,
		wedgeprops = {"edgecolor" : "black",
					'linewidth': 2,
					'antialiased': True})

# Equal aspect ratio ensures
# that pie is drawn as a circle.
plt.axis('equal')

# Display the graph onto the screen
plt.show()
