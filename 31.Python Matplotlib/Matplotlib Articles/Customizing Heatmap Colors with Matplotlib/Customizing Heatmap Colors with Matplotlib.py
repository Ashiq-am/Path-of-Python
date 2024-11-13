import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# Load a sample dataset from Seaborn
data = sns.load_dataset("flights")

# Pivot the dataset to create a matrix
data_pivot = data.pivot(index="month", columns="year", values="passengers")

# Create a custom colormap
colors = ["#ffffcc", "#a1dab4", "#41b6c4", "#2c7fb8", "#253494"]  # Define custom colors
custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)  # Create custom colormap

# Adjust color limits
vmin = data_pivot.min().min()  # Minimum value in the dataset
vmax = data_pivot.max().max()  # Maximum value in the dataset

# Create the heatmap
plt.imshow(data_pivot, cmap=custom_cmap, vmin=vmin, vmax=vmax)

# Add colorbar
cbar = plt.colorbar(label='Passengers')

# Add labels and title
plt.title('Passenger Flights')
plt.xlabel('Year')
plt.ylabel('Month')

# Customize tick labels
plt.xticks(range(len(data_pivot.columns)), data_pivot.columns, rotation=45)
plt.yticks(range(len(data_pivot.index)), data_pivot.index)

# Add annotations
for i in range(len(data_pivot.index)):
    for j in range(len(data_pivot.columns)):
        plt.text(j, i, data_pivot.iloc[i, j], ha="center", va="center", color="black")

# Customize grid appearance
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Set logarithmic scale for the colorbar
cbar.ax.set_yscale('log')

# Display the plot
plt.show()
