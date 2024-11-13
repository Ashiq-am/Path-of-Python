import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
g = sns.PairGrid(tips, vars=["total_bill", "tip", "size"], hue="sex")

# Map a scatterplot to each cell
g.map(sns.scatterplot)

# Add a title and labels
g.set_title("Relationships Between Total Bill, Tip, and Size by Sex")
g.set_axis_labels("Total Bill (USD)", "Tip (USD)", "Size")

plt.show()
