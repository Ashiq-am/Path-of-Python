import seaborn as sns
import matplotlib.pyplot as plt

# Create a histogram
sns.histplot(data=tips, x="total_bill")

# Display the plot
plt.show()
