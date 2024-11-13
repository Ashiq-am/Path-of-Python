import seaborn as sns
import matplotlib.pyplot as plt

# Create a KDE plot
sns.kdeplot(data=tips, x="total_bill")

# Display the plot
plt.show()
