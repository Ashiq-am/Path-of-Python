import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Create boxplots
sns.boxplot(x='day', y='total_bill', data=tips, ax=ax1)
sns.boxplot(x='day', y='tip', data=tips, ax=ax2)

# Add titles to each subplot
ax1.set_title('Total Bill Distribution by Day')
ax2.set_title('Tip Distribution by Day')

plt.show()
