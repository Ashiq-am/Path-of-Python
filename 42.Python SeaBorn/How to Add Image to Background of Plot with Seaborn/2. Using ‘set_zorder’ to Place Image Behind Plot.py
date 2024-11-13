import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')

# Load background image
bg_image = plt.imread('/content/gfglogo.png')

# Create figure and axes
fig, ax = plt.subplots()

# Plot data
sns.scatterplot(data=tips, x='total_bill', y='tip', ax=ax)

# Display the background image
ax.imshow(bg_image, extent=ax.get_xlim() + ax.get_ylim(), aspect='auto', zorder=-1)

plt.show()
