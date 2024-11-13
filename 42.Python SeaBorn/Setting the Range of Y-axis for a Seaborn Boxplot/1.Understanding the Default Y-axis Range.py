import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
data = sns.load_dataset('tips')

# Create a simple boxplot
sns.boxplot(x='day', y='total_bill', data=data)
plt.show()
