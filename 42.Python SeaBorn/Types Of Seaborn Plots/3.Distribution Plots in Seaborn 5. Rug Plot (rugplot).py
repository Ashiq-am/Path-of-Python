import seaborn as sns
import matplotlib.pyplot as plt

# Create a rug plot
sns.rugplot(data=tips, x="total_bill")

# Display the plot
plt.show()
