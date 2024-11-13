import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a pair plot
sns.pairplot(tips, hue="smoker", palette="coolwarm")

# Display the plot
plt.show()
