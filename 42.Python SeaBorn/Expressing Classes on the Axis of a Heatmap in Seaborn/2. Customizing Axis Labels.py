import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
flights = sns.load_dataset("flights")
flights_df = flights.pivot(index="month", columns="year", values="passengers")

# Create a heatmap with customized axis labels
plt.figure(figsize=(10,6))
sns.heatmap(flights_df.corr(), cmap="inferno", annot=True, linewidth=2,
            cbar_kws={"shrink": .8, 'extend': 'max', 'extendfrac': .2, "drawedges": True})
plt.title("Heatmap Correlation of 'Flights' Dataset", fontsize=25, pad=20)
plt.xlabel("Years", fontsize=20)
plt.ylabel("Months", fontsize=20)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()
