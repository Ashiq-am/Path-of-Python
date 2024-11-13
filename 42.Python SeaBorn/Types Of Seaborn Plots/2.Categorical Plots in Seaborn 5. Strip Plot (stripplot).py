import seaborn as sns
import matplotlib.pyplot as plt

# Create a strip plot
sns.stripplot(data=tips, x="day", y="total_bill")

# Display the plot
plt.show()
