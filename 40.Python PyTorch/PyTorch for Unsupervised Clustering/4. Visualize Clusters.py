# Visualize clusters
plt.scatter(data[:, 0], data[:, 1], c=labels.numpy(), cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, color='red')
plt.show()
