import matplotlib.pyplot as plt

# Setting labels for items in Chart
Employee = ['Roshni', 'Shyam', 'Priyanshi',
			'Harshit', 'Anmol']

# Setting size in Chart based on
# given values
Salary = [40000, 50000, 70000, 54000, 44000]

# colors
colors = ['#FF0000', '#0000FF', '#FFFF00',
		'#ADFF2F', '#FFA500']
# explosion
explode = (0.05, 0.05, 0.05, 0.05, 0.05)

# Pie Chart
plt.pie(Salary, colors=colors, labels=Employee,
		autopct='%1.1f%%', pctdistance=0.85,
		explode=explode)

# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()

# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)

# Adding Title of chart
plt.title('Employee Salary Details')

# Displaing Chart
plt.show()
