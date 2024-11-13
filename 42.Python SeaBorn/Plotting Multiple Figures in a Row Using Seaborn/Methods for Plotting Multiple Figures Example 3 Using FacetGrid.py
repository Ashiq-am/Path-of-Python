# Load the example dataset
tips = sns.load_dataset("tips")

# Create a FacetGrid
g = sns.FacetGrid(tips, col="time", row="smoker")
g.map(sns.scatterplot, "total_bill", "tip")

# Display the plot
plt.show()
