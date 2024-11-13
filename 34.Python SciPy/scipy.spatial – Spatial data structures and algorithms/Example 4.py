from scipy.spatial import KDTree

points = np.random.rand(10, 2)
kdtree = KDTree(points)
result = kdtree.query((1, 1))
print(result)
