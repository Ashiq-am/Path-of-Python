import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')

# Define a custom color palette using RGB values
custom_palette = [(0.2, 0.4, 0.6), (0.4, 0.6, 0.8), (0.6, 0.8, 1.0), (0.8, 1.0, 0.6)]

# Create a boxplot with the custom color palette
sns.boxplot(x='day', y='total_bill', data=tips, palette=custom_palette)
plt.show()
