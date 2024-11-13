# importing modules
from matplotlib import pyplot as plt

# assigning x and y coordinates
foodPreferance = ['Vegetarian', 'Non Vegetarian',
								'Vegan', 'Eggitarian']

consumers = [30, 100, 10, 60]

# depicting the visualization
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')
ax.pie(consumers, labels = foodPreferance,
	autopct='%1.2f%%')

# displaying the title
plt.title("Society Food Preferance",
		fontsize = 10)
