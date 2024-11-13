import seaborn as sns
import matplotlib.pyplot as plt

# Create a line plot
sns.lineplot(data=tips, x="size", y="tip")

# Display the plot
plt.show()
