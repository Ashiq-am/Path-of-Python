import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create a relational plot
sns.relplot(x="total_bill", y="tip", data=tips, hue="smoker", style="time", size="size")
plt.show()
