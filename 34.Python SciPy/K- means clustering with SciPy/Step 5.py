# assign centroids and clusters
centroids, clusters = kmeans2(data, 3,
							minit='random')

print("Centroids :\n", centroids, "\n")
print("Clusters :", clusters)
