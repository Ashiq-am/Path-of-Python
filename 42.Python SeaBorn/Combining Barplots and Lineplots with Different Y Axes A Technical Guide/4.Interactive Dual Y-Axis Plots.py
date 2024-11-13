import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mplcursors

data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Revenue': [1000, 1500, 2000, 2500],
    'New Subscribers': [300, 400, 500, 600]
}

df = pd.DataFrame(data)
fig, ax1 = plt.subplots()

# Create barplot for revenue with updated color
sns.barplot(x='Product', y='Revenue', data=df, ax=ax1, color='lightgreen')
ax1.set_ylabel('Quarterly Revenue ($)', fontsize=12, color='green')
ax1.set_xlabel('Product', fontsize=12, color='black')

# Create secondary y-axis
ax2 = ax1.twinx()

# Create lineplot for new subscribers with updated color and labels
sns.lineplot(x='Product', y='New Subscribers', data=df, ax=ax2, color='orange', marker='o')
ax2.set_ylabel('Number of New Subscribers', fontsize=12, color='orange')

# Adjust the scale of the secondary y-axis if needed
ax2.set_ylim(250, 650)

# Change axis and tick colors to match the data plots
ax1.yaxis.label.set_color('green')
ax2.yaxis.label.set_color('orange')
ax1.tick_params(axis='y', colors='green')
ax2.tick_params(axis='y', colors='orange')

plt.title('Quarterly Revenue and New Subscribers by Product', fontsize=14)
mplcursors.cursor(hover=True)
plt.show()
