import seaborn as sns
import matplotlib.pyplot as plt

# Create a diverging palette
palette = sns.diverging_palette(240, 10, n=9)

# Display the palette
sns.palplot(palette)
plt.show()
