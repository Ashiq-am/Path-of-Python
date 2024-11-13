import seaborn as sns
import matplotlib.pyplot as plt

# Create an ECDF plot
sns.ecdfplot(data=tips, x="total_bill")

# Display the plot
plt.show()
