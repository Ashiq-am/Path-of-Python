import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# Use Matplotlib's style to set grid
plt.style.use('seaborn-whitegrid')

# Create a plot with 'sex' as a factor
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')

plt.show()
