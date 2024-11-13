from scipy.interpolate import splprep

# Define parametric data
x = np.array([87., 98., 100., 95., 100., 108., 110., 118., 120., 117., 105., 100., 92., 90.])
y = np.array([42., 35., 32., 25., 18., 20., 27., 27., 35., 46., 45., 48., 55., 51.])

# Create parametric spline representation
spline_params = splprep([x, y], s=0)[0]

# Evaluate spline at equal arc-length intervals
points = splev(np.linspace(0, len(x), num=100), spline_params)

plt.plot(points[0], points[1])
plt.scatter(x, y)
plt.title('Parametric Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
