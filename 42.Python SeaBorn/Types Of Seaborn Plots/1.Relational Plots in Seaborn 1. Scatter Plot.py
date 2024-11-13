import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset for the scatter plot
tips = sns.load_dataset("tips")

# Create a scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip")

# Display the plot
plt.show()
