# Creating Dendrogram for our data
# Z = linkage matrix
Z = hierarchy.linkage(data, method='average')

plt.figure()
plt.title("Dendrograms")

# Dendrogram plotting using linkage matrix
dendrogram = hierarchy.dendrogram(Z)
