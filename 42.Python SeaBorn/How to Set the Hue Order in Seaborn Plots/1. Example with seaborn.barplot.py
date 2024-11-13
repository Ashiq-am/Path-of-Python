import seaborn as sns
import matplotlib.pyplot as plt

# Example data
tips = sns.load_dataset("tips")

# Specify the desired hue order
hue_order = ["Female", "Male"]

# Plot with specified hue order
sns.barplot(x="day", y="total_bill", hue="sex", data=tips)

# Show the plot
plt.show()
