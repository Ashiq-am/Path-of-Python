import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load sample data
flights = sns.load_dataset("flights")

# Pivot the data correctly
data = flights.pivot(index="month", columns="year", values="passengers")

# Create a basic heatmap
sns.heatmap(data)
plt.title("Basic Heatmap")
plt.show()
