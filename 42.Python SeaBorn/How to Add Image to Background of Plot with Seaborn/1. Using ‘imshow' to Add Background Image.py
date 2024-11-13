import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')

# Load background image
bg_image = plt.imread('/content/gfglogo.png')

# Create figure and axes
fig, ax = plt.subplots()

# Display the background image
ax.imshow(bg_image, extent=[0, 1, 0, 1], aspect='auto')

# Plot data
sns.scatterplot(data=tips, x='total_bill', y='tip', ax=ax)

# Adjust the plot limits to fit the background image
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
