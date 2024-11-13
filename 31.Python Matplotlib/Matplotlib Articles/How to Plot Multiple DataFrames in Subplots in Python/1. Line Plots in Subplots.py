import pandas as pd
import matplotlib.pyplot as plt

# Example dataframes
df1 = pd.DataFrame({'x': range(10), 'y1': range(10)})
df2 = pd.DataFrame({'x': range(10), 'y2': range(10, 20)})
df3 = pd.DataFrame({'x': range(10), 'y3': range(20, 30)})

# Create a figure with subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 10))

# Plot each dataframe on its subplot
axs[0].plot(df1['x'], df1['y1'], marker='o', linestyle='-', color='b', label='df1')
axs[0].set_title('Dataframe 1')
axs[0].legend()

axs[1].plot(df2['x'], df2['y2'], marker='s', linestyle='--', color='r', label='df2')
axs[1].set_title('Dataframe 2')
axs[1].legend()

axs[2].plot(df3['x'], df3['y3'], marker='^', linestyle=':', color='g', label='df3')
axs[2].set_title('Dataframe 3')
axs[2].legend()

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
