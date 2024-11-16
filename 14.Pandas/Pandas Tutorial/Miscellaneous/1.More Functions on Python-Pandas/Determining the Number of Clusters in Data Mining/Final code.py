# clustering the data using Kmeans
# using k = 5
model = KMeans(n_clusters=5)

# predicting the clusters
pred = model.fit_predict(dataset_new)

# plotting all the clusters
colours = ['red', 'blue', 'green', 'yellow', 'orange']

for i in np.unique(model.labels_):
    plt.scatter(dataset_new[pred == i, 0],
                dataset_new[pred == i, 1],
                c=colours[i])

# plotting the cluster centroids
plt.scatter(model.cluster_centers_[:, 0],
            model.cluster_centers_[:, 1],
            s=200,  # marker size
            c='black')

plt.title('K Means clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()
