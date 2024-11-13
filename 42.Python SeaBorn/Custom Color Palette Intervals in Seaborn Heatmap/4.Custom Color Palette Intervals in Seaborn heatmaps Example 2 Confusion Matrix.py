import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, BoundaryNorm
from sklearn.metrics import confusion_matrix

y_true = [0, 1, 2, 2, 0, 1, 1, 2, 0, 1]
y_pred = [0, 2, 1, 2, 0, 0, 1, 2, 0, 2]
conf_matrix = confusion_matrix(y_true, y_pred)

# Define data ranges and corresponding colors
bounds = [0, 1, 2, 3, 4, 5]
colors = ["#fee08b", "#fdae61", "#f46d43", "#d73027", "#a50026"]
custom_palette = LinearSegmentedColormap.from_list("custom_palette", colors)
norm = BoundaryNorm(bounds, custom_palette.N)

# Create the heatmap with custom intervals
sns.heatmap(conf_matrix, cmap=custom_palette, norm=norm, annot=True, fmt='d')
plt.title("Confusion Matrix with Custom Color Palette Intervals")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()
