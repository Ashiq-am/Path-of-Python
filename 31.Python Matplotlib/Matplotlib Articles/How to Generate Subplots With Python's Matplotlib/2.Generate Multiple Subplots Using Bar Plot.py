import matplotlib.pyplot as plt
import numpy as np

# Example data for bar plots
categories = ['A', 'B', 'C', 'D']
values1 = [3, 7, 1, 5]
values2 = [5, 2, 8, 4]
values3 = [2, 6, 3, 9]
values4 = [8, 4, 6, 2]

# Creating Multiple Subplots for Bar Plots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Bar Plot 1
axes[0, 0].bar(categories, values1, color='blue')
axes[0, 0].set_title('Bar Plot 1')

# Bar Plot 2
axes[0, 1].bar(categories, values2, color='orange')
axes[0, 1].set_title('Bar Plot 2')

# Bar Plot 3
axes[1, 0].bar(categories, values3, color='green')
axes[1, 0].set_title('Bar Plot 3')

# Bar Plot 4
axes[1, 1].bar(categories, values4, color='red')
axes[1, 1].set_title('Bar Plot 4')

# Adjusting layout
plt.tight_layout()

# Show the plots
plt.show()
