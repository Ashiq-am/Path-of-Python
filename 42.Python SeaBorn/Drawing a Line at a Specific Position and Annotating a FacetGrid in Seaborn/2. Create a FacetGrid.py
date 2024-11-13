# Create a FacetGrid
g = sns.FacetGrid(tips, col="time")
g.map(sns.histplot, "total_bill")

plt.show()
