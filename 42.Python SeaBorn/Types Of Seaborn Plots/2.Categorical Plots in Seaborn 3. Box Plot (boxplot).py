import seaborn as sns
import matplotlib.pyplot as plt

# Create a box plot
sns.boxplot(data=tips, x="day", y="total_bill")

# Display the plot
plt.show()
