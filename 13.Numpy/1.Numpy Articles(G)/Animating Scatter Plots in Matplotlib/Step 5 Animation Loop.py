points += 0.1 * (np.random.random((2, numpoints)) - 0.5)
plt.scatter(*points, c=colors, s=100)
camera.snap()
