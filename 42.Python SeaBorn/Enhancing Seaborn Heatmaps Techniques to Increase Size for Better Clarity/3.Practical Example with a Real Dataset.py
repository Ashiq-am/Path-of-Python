import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
flights = sns.load_dataset("flights")
data = flights.pivot(index="month", columns="year", values="passengers")

# Create a heatmap with increased size
fig, ax = plt.subplots(figsize=(15, 10))
sns.heatmap(data, annot=True, fmt="d", linewidths=.5, ax=ax)
plt.show()
