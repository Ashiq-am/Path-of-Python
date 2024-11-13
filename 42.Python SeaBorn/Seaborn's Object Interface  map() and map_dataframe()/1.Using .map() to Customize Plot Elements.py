import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

g = sns.FacetGrid(tips, col="time")
g.map(sns.kdeplot, "total_bill", shade=True, color="orange", bw_adjust=0.5)
g.set_axis_labels("Total Bill", "Density")
g.set_titles("{col_name} Time")
plt.show()
