from scipy.cluster.hierarchy import fcluster

# Form flat clusters by cutting the dendrogram at a specified distance
max_distance = 1.5
clusters = fcluster(Z, max_distance, criterion='distance')

# Plot the clustered data
plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap='rainbow')
plt.title('Data Points Clustered Using Agglomerative Clustering')
plt.show()
