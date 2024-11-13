import matplotlib.pyplot as plt

# List of 7-days
days = [x for x in range(0, 7)]

# List of Suspected cases
Suspected = [12, 18, 35, 50, 72, 90, 100]

# List of Cured Cases
Cured = [4, 8, 15, 22, 41, 55, 62]

# List of Number of deaths
Deaths = [1, 3, 5, 7, 9, 11, 13]

# Plot x-labels, y-label and data
plt.plot([], [], color ='blue',
		label ='Suspected')
plt.plot([], [], color ='orange',
		label ='Cured')
plt.plot([], [], color ='brown',
		label ='Deaths')

# Implementing stackplot on data
plt.stackplot(days, Suspected, Cured,
			Deaths, baseline ='zero',
			colors =['blue', 'orange',
					'brown'])

plt.legend()

plt.title('No of Cases')
plt.xlabel('Day of the week')
plt.ylabel('Overall cases')

plt.show()
