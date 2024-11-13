import seaborn as sns
import matplotlib.pyplot as plt

# Create a distribution plot
sns.displot(data=tips, x="total_bill", kind="kde")

# Display the plot
plt.show()
