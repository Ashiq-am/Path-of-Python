import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')

# Create a boxplot with a specific color
sns.boxplot(x='day', y='total_bill', data=tips, color='skyblue')
plt.show()
