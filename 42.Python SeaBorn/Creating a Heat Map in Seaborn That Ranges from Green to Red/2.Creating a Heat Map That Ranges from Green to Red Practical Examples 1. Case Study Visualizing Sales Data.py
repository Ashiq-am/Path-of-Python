import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import pandas as pd

# Sample sales data
data = {
    "Jan": [200, 150, 300, 400],
    "Feb": [180, 160, 320, 350],
    "Mar": [210, 170, 330, 420],
    "Apr": [220, 180, 340, 430]
}
regions = ["North", "South", "East", "West"]
df = pd.DataFrame(data, index=regions)

# Define colormap
cmap = mcolors.LinearSegmentedColormap.from_list("green_red", ["green", "red"], N=100)
plt.figure(figsize=(10, 6))
sns.heatmap(df, cmap=cmap, annot=True, fmt="d", linewidths=.5)
plt.title("Monthly Sales Data by Region")
plt.show()
