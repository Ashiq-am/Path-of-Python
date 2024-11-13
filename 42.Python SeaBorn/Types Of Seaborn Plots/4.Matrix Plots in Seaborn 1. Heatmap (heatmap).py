import seaborn as sns
import matplotlib.pyplot as plt

# Load the example flights dataset
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

# Create a heatmap
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")

# Display the plot
plt.show()
