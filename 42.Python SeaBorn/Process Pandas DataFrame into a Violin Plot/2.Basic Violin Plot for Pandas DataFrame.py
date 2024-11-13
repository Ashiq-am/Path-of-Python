import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the violin plot
sns.violinplot(x='Group', y='Values', data=df)

# Display the plot
plt.show()
