plt.figure(figsize=(10, 6))

for idx, column in enumerate(df.columns):
    plt.plot(df.index, df[column], label=column, color=colors[idx], linestyle=linestyles[idx], marker='o')

# Adding gridlines
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adding labels, title, and legend
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Improved Wide DataFrame Plot with Colors, Linestyles, and Markers')
plt.legend(loc='upper left')

# Display the plot
plt.show()
