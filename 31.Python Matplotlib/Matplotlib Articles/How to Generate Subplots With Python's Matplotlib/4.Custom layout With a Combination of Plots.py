import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Example data for bar plots
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 1, 5]

# Example data for pie chart
labels = ['Category 1', 'Category 2', 'Category 3']
sizes = [30, 40, 30]

# Example data for custom layout
x_custom = np.linspace(0, 5, 50)
y3 = x_custom**2
y4 = np.exp(x_custom)

# Creating Multiple Subplots
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 8))

# Creating Multiple Subplots of Line Plots
axes[0, 0].plot(x, y1, label='sin(x)', color='blue')
axes[0, 0].set_title('Line Plot 1')
axes[0, 0].legend()

axes[0, 1].plot(x, y2, label='cos(x)', color='orange')
axes[0, 1].set_title('Line Plot 2')
axes[0, 1].legend()

# Creating Multiple Subplots of Bar Plots
axes[0, 2].bar(categories, values, color='green')
axes[0, 2].set_title('Bar Plot')

# Creating Multiple Subplots of Pie Charts
axes[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['red', 'yellow', 'green'])
axes[1, 0].set_title('Pie Chart')

# Creating a custom Multiple Subplots
axes[1, 1].plot(x_custom, y3, label='x^2', color='purple')
axes[1, 1].set_title('Custom Plot 1')
axes[1, 1].legend()

axes[1, 2].plot(x_custom, y4, label='e^x', color='brown')
axes[1, 2].set_title('Custom Plot 2')
axes[1, 2].legend()

# Adjusting layout
plt.tight_layout()

# Show the plots
plt.show()
