import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# Define a custom plotting function with specific arguments
def scatterplot(data,color, marker='o', size=50):
    plt.scatter(data["total_bill"], data["tip"], color=color, marker=marker, s=size)

g = sns.FacetGrid(tips, col="time") # Plot using .map_dataframe()
g.map_dataframe(scatterplot, color="skyblue", marker='o', size=30)
g.set_axis_labels("Total Bill", "Tip")
plt.show()
