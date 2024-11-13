import pandas as pd
import matplotlib.pyplot as plt

# Example dataframes
df1 = pd.DataFrame({'x': range(10), 'y1': range(10)})
df2 = pd.DataFrame({'x': range(10), 'y2': range(10, 20)})

# Create a figure with subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot scatter plots for each dataframe
axs[0].scatter(df1['x'], df1['y1'], color='b', label='df1')
axs[0].set_title('Dataframe 1')
axs[0].legend()

axs[1].scatter(df2['x'], df2['y2'], color='r', label='df2')
axs[1].set_title('Dataframe 2')
axs[1].legend()

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
