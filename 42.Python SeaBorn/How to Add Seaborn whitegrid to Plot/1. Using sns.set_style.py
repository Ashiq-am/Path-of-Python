import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# Set the style to whitegrid
sns.set_style('whitegrid')

# Create a plot
sns.scatterplot(data=tips, x='total_bill', y='tip')

plt.show()
