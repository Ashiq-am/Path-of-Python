# Create a diverging palette with a custom center point
palette = sns.diverging_palette(240, 10, center="dark", n=9)

# Display the palette
sns.palplot(palette)
plt.show()
