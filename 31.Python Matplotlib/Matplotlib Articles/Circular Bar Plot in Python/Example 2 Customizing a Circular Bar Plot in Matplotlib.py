import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [20, 35, 30, 25]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Custom colors for bars

# Create a circular bar plot
fig, ax = plt.subplots(subplot_kw=dict(polar=True))
bars = ax.bar(np.arange(len(categories)) * 2 * np.pi /
              len(categories), values, color=colors, alpha=1)

# Add labels to each bar
for i, (label, angle) in enumerate(zip(categories, np.arange(len(categories)) * 2 * np.pi / len(categories))):
    x = angle
    y = values[i] + 1  # Adjust height for label placement
    ax.text(x, y, label, ha='center', va='center', fontsize=8, color='black')

# Customizing the plot
ax.set_theta_offset(np.pi / 2)  # Offset to start the bars from the top
ax.set_theta_direction(-1)  # Clockwise direction for bars
# Adjust the y-axis limit for better visualization
ax.set_ylim(0, max(values) + 5)
ax.set_yticks([])  # Hide the y-axis ticks
ax.spines['polar'].set_visible(False)  # Hide the polar axis line

plt.show()
