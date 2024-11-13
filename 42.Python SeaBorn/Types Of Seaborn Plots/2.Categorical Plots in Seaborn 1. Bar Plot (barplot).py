import seaborn as sns
import matplotlib.pyplot as plt

# Create a bar plot
sns.barplot(data=tips, x="day", y="total_bill")

# Display the plot
plt.show()
