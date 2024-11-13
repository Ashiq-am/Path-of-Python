# code book generation
centroids, mean_value = kmeans(data, 3)

print("Code book :\n", centroids, "\n")
print("Mean of Euclidean distances :",
	mean_value.round(4))
