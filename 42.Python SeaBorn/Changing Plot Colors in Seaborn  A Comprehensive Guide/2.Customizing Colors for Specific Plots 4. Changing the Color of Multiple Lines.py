df = pd.DataFrame({
    'day': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'store': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'sales': [3, 3, 5, 4, 7, 6, 8, 9, 12, 13]
})

# Create a line plot with the mako_r color palette
palette = sns.color_palette("mako_r", 2)
sns.lineplot(data=df, x='day', y='sales', hue='store', palette=palette, linewidth=2.5, style='store', markers=True)

# Customizing the plot further
plt.title('Sales Trends by Store', fontsize=16)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Sales', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Store', title_fontsize='13', loc='upper left')
plt.show()
