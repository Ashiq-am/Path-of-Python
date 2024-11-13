import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="smoker", row="sex", margin_titles=True)

# Map a plotting function to each facet
g = g.map(plt.scatter, "total_bill", "tip", color="m")

# Set the title using suptitle
g.fig.suptitle("Value of Tips Given to Waiters, by Days of the Week and Sex", fontsize=24)
g.fig.subplots_adjust(top=0.9)
plt.show()
