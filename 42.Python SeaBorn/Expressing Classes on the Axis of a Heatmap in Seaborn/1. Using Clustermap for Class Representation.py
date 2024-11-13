import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
flights = sns.load_dataset("flights")
flights_df = flights.pivot(index="month", columns="year", values="passengers")

# Create class labels (example: seasons)
seasons = ['Winter', 'Spring', 'Summer', 'Fall'] * 3
season_colors = {'Winter': 'blue', 'Spring': 'green', 'Summer': 'red', 'Fall': 'orange'}
label_cols = pd.Series(seasons, index=flights_df.columns).map(season_colors)

# Create a clustermap with class information on the axis
sns.clustermap(flights_df.corr(), row_colors=label_cols, col_colors=label_cols,
               row_cluster=False, col_cluster=False)
plt.figure(figsize=(8,6))
plt.show()
