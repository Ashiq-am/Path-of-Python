import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Function to interactively define color mappings
def define_color_mapping():
    print("Define color mappings for values 0 to 5:")
    cmap_dict = {}
    for i in range(6):
        color = input(f"Enter color for value {i}: ").strip()
        cmap_dict[i] = color
    return cmap_dict

data = np.random.randint(0, 6, size=(10, 10))

# Get custom color mappings interactively
cmap_dict = define_color_mapping()
cmap = sns.color_palette([cmap_dict[i] for i in range(6)])

sns.heatmap(data, cmap=cmap, vmin=0, vmax=5, cbar=False, annot=False)
plt.title('Custom Color Mappings in Seaborn Heatmap')
plt.show()
