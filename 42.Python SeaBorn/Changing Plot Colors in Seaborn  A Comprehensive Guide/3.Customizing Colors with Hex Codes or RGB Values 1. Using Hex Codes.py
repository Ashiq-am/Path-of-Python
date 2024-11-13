import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')

# Define a custom color palette using hex codes
custom_palette = ['#FF6347', '#4682B4', '#8A2BE2', '#FFD700']

# Create a boxplot with the custom color palette
sns.boxplot(x='day', y='total_bill', data=tips, palette=custom_palette)
plt.show()
