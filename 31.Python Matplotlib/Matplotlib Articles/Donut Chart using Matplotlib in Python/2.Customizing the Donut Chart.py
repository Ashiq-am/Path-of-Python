import matplotlib.pyplot as plt


# Setting size in Chart based on
# given values
sizes = [100, 500, 70, 54, 440]

# Setting labels for items in Chart
labels = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']

# colors
colors = ['#FF0000', '#0000FF', '#FFFF00', '#ADFF2F', '#FFA500']

# explosion
explode = (0.05, 0.05, 0.05, 0.05, 0.05)

# Pie Chart
plt.pie(sizes, colors=colors, labels=labels,
		autopct='%1.1f%%', pctdistance=0.85,
		explode=explode)

# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()

# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)

# Adding Title of chart
plt.title('Favourite Fruit Survey')

# Add Legends
plt.legend(labels, loc="upper right")

# Displaing Chart
plt.show()
