import pandas as pd
import matplotlib.pyplot as plt

# Example dataframes
df1 = pd.DataFrame({'category': ['A', 'B', 'C'], 'values': [10, 20, 15]})
df2 = pd.DataFrame({'category': ['A', 'B', 'C'], 'values': [15, 18, 12]})

# Create a figure with subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot bar charts for each dataframe
axs[0].bar(df1['category'], df1['values'], color='b', alpha=0.7, label='df1')
axs[0].set_title('Dataframe 1')
axs[0].legend()

axs[1].bar(df2['category'], df2['values'], color='r', alpha=0.7, label='df2')
axs[1].set_title('Dataframe 2')
axs[1].legend()

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
