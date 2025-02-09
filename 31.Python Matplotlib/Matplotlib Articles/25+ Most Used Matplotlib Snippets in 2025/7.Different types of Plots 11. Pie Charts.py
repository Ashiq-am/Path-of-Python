import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
plt.title('Pie Chart')
plt.show()