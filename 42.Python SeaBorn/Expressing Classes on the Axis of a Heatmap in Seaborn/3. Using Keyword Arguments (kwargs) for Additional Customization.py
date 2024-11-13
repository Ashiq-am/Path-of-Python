import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
flights = sns.load_dataset("flights")
flights_df = flights.pivot(index="month", columns="year", values="passengers")

# Define additional keyword arguments for customization
kwargs = {
    'alpha': .9,
    'linestyle': '--',
    'rasterized': False,
    'edgecolor': 'w',
    "capstyle": 'projecting'
}

# Create a heatmap with customized axis labels and kwargs
plt.figure(figsize=(10,6))
ax = sns.heatmap(flights_df.corr(), cmap="inferno", annot=True, linewidths=2, **kwargs)
plt.title("Heatmap Correlation of 'Flights' Dataset", fontsize=25, pad=20)
plt.xlabel("Years", fontsize=20)
plt.ylabel("Months", fontsize=20)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()
