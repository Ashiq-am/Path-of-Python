# observations
data = np.array([[1, 3, 4, 5, 2],
				[2, 3, 1, 6, 3],
				[1, 5, 2, 3, 1],
				[3, 4, 9, 2, 1]])

# normalize
data = whiten(data)

print(data)
