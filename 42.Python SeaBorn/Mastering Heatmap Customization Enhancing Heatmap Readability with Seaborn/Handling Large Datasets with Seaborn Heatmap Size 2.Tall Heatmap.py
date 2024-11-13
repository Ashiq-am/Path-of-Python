import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = sns.load_dataset("flights")
data = data.pivot(index="month", columns="year", values="passengers")
# Set a taller heatmap
plt.figure(figsize=(6, 14))
sns.heatmap(data, annot=True, fmt="d", cmap="YlGnBu")
plt.show()
