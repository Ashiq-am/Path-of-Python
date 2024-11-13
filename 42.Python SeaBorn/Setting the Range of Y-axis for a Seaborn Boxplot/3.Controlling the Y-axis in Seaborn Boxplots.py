import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
data = sns.load_dataset('tips')

# Create a boxplot
sns.boxplot(x='day', y='total_bill', data=data)

# Set the range of y-axis to focus on bills between $10 and $40
plt.ylim(10, 40)

# Show the plot
plt.show()
