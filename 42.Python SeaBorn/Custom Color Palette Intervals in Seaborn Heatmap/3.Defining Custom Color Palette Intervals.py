import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, BoundaryNorm
import pandas as pd

# Load the "flights" dataset from Seaborn
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

# Define custom colors and intervals
colors = ["#d73027", "#f46d43", "#fdae61", "#fee08b", "#d9ef8b", "#a6d96a", "#66bd63", "#1a9850", "#006837"]
boundaries = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
cmap = LinearSegmentedColormap.from_list("custom", colors, N=len(colors))
norm = BoundaryNorm(boundaries, cmap.N, clip=True)

# Create the heatmap with advanced customizations
plt.figure(figsize=(14, 8))
ax = sns.heatmap(flights_pivot, cmap=cmap, norm=norm, annot=True, fmt="d", linewidths=.5, cbar_kws={"shrink": .8})

# Add titles and labels
plt.title("Monthly Airline Passenger Numbers (1949-1960)", fontsize=18)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Month", fontsize=14)

# Customize the x and y axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=12)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=12)

# Customize the colorbar
cbar = ax.collections[0].colorbar
cbar.set_label('Number of Passengers', rotation=270, fontsize=14, labelpad=15)
cbar.set_ticks(boundaries)
cbar.set_ticklabels(['100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700-800', '800-900', '900-1000', '1000+'])

# Add custom annotations
for y in range(flights_pivot.shape[0]):
    for x in range(flights_pivot.shape[1]):
        value = flights_pivot.iloc[y, x]
        ax.text(x + 0.5, y + 0.5, f'{value}', color='black', ha='center', va='center', fontsize=10)

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()
