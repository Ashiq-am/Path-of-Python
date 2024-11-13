import seaborn as sns
import matplotlib.pyplot as plt
sns.load_dataset("tips")

# Create a relational plot
sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker")

# Display the plot
plt.show()
