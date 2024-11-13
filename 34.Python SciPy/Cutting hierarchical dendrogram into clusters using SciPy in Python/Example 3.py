# Creating Dendrogram for our data
# max_d = cut-off/ Threshold value
max_d = 4

Z = hierarchy.linkage(data, method='average')
plt.figure()
plt.title("Dendrograms")
dendrogram = hierarchy.dendrogram(Z)

# Cutting the dendrogram at max_d
plt.axhline(y=max_d, c='k')
