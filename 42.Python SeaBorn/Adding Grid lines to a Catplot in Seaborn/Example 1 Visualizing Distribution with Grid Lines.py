import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Create the catplot
g = sns.catplot(x="day", y="total_bill", kind="boxen", data=tips)

# Access the axes object
ax = g.ax

# Add horizontal grid lines
ax.grid(True, axis="y", linestyle="--")
plt.show()
