# determining the maximum number of clusters
# using the simple method
limit = int((dataset_new.shape[0]//2)**0.5)

# determing number of clusters
# using silhouette score method
for k in range(2, limit+1):
	model = KMeans(n_clusters=k)
	model.fit(dataset_new)
	pred = model.predict(dataset_new)
	score = silhouette_score(dataset_new, pred)
	print('Silhouette Score for k = {}: {:<.3f}'.format(k, score))
