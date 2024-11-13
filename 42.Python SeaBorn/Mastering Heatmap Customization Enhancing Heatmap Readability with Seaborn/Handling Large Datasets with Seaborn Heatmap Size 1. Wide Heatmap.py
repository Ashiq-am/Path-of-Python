import seaborn as sns
import pandas as pd

data = sns.load_dataset("flights")
data = data.pivot(index="month", columns="year", values="passengers")
# Set a wider heatmap
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))
sns.heatmap(data, annot=True, fmt="d", cmap="YlGnBu")
plt.show()
