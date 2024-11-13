# Create a diverging palette with custom saturation and lightness
palette = sns.diverging_palette(100, 5, s=100, l=40, n=9)

# Display the palette
sns.palplot(palette)
plt.show()
