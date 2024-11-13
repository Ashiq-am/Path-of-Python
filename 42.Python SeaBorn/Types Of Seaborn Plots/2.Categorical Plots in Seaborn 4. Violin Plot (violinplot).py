import seaborn as sns
import matplotlib.pyplot as plt

# Create a violin plot
sns.violinplot(data=tips, x="day", y="total_bill")

# Display the plot
plt.show()
