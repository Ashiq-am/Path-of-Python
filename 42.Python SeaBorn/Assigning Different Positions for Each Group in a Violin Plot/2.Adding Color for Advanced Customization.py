# Define custom colors
colors = ['lightblue', 'lightgreen', 'lightcoral']

# Custom positions for each group
positions = [1, 3, 5]

# Use the 'positions' argument within a Matplotlib call instead of Seaborn
plt.xticks(positions, ['A', 'B', 'C']) # Set the xticks to the desired positions and labels

sns.violinplot(x='Group', y='Values', data=data, palette=colors) # Call violinplot without the positions argument
plt.show()
