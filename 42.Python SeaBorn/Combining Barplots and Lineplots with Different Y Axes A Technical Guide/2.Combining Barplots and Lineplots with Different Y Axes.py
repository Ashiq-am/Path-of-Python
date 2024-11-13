import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue': [20000, 21000, 19000, 22000, 21500, 23000],
    'New Subscribers': [450, 520, 480, 500, 490, 530]
}
df = pd.DataFrame(data)

# Create figure and primary y-axis
fig, ax1 = plt.subplots()

# Create barplot for revenue
sns.barplot(x='Month', y='Revenue', data=df, ax=ax1, color='skyblue')
ax1.set_ylabel('Monthly Revenue ($)', fontsize=12, color='blue')

# Create secondary y-axis
ax2 = ax1.twinx()

# Create lineplot for new subscribers
sns.lineplot(x='Month', y='New Subscribers', data=df, ax=ax2, color='coral', marker='o')
ax2.set_ylabel('Number of New Subscribers', fontsize=12, color='darkred')

# Adjust the scale of the secondary y-axis
ax2.set_ylim(400, 600)

# Change axis and tick colors to match the data plots
ax1.yaxis.label.set_color('blue')
ax2.yaxis.label.set_color('darkred')
ax1.tick_params(axis='y', colors='blue')
ax2.tick_params(axis='y', colors='darkred')

# Display the plot
plt.show()
