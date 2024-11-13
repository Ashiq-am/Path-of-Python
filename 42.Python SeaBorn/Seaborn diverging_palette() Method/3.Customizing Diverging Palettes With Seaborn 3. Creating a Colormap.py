data = np.random.randn(10, 10)

# Define the diverging colormap
cmap = sns.diverging_palette(150, 12, as_cmap=True)
plt.figure(figsize=(8, 6))
sns.heatmap(data, cmap=cmap, center=0)
plt.title('Heatmap with Diverging Colormap')
plt.show()
