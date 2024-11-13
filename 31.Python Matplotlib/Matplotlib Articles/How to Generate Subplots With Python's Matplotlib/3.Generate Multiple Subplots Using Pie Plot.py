import matplotlib.pyplot as plt

# Example data for pie charts
labels1 = ['Category 1', 'Category 2', 'Category 3']
sizes1 = [30, 40, 30]

labels2 = ['Section A', 'Section B', 'Section C']
sizes2 = [20, 50, 30]

labels3 = ['Apple', 'Banana', 'Orange', 'Grapes']
sizes3 = [25, 30, 20, 25]

labels4 = ['Red', 'Green', 'Blue']
sizes4 = [40, 30, 30]

# Creating Multiple Subplots for Pie Charts
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Pie Chart 1
axes[0, 0].pie(sizes1, labels=labels1, autopct='%1.1f%%', colors=['red', 'yellow', 'green'])
axes[0, 0].set_title('Pie Chart 1')

# Pie Chart 2
axes[0, 1].pie(sizes2, labels=labels2, autopct='%1.1f%%', colors=['blue', 'orange', 'purple'])
axes[0, 1].set_title('Pie Chart 2')

# Pie Chart 3
axes[1, 0].pie(sizes3, labels=labels3, autopct='%1.1f%%', colors=['orange', 'yellow', 'green', 'purple'])
axes[1, 0].set_title('Pie Chart 3')

# Pie Chart 4
axes[1, 1].pie(sizes4, labels=labels4, autopct='%1.1f%%', colors=['red', 'green', 'blue'])
axes[1, 1].set_title('Pie Chart 4')

# Adjusting layout
plt.tight_layout()

# Show the plots
plt.show()
