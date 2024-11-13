# Define colors and linestyles for each series
colors = ['blue', 'green', 'red']
linestyles = ['-', '--', '-.']

# Plotting the DataFrame
plt.figure(figsize=(10, 6))

for idx, column in enumerate(df.columns):
    plt.plot(df.index, df[column], label=column, color=colors[idx], linestyle=linestyles[idx])

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Wide DataFrame Plot with Colors and Linestyles')

# Adding a legend
plt.legend()

# Display the plot
plt.show()
