import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')

# Set a color palette
sns.set_palette("husl")

# Create a boxplot with the new color palette
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()
