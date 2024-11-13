# mapping the centroids
clusters, distances = vq(data, centroids)

print("Cluster index :", clusters, "\n")
print("Distance from the centroids :", distances)
