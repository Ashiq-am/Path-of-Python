import seaborn as sns
import matplotlib.pyplot as plt

# Load the example flights dataset
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

# Create a cluster map
sns.clustermap(flights_pivot, cmap="viridis", standard_scale=1)

# Display the plot
plt.show()
