import seaborn as sns
import matplotlib.pyplot as plt

# Create a count plot
sns.countplot(data=tips, x="day")

# Display the plot
plt.show()
