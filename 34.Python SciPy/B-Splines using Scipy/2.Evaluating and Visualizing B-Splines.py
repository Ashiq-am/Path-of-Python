from scipy.interpolate import splrep, splev

# Sample data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Find spline representation
tck = splrep(x, y)

# Evaluate spline at new points
xnew = np.linspace(0, 10, 200)
ynew = splev(xnew, tck)

# Plotting
plt.plot(xnew, ynew)
plt.scatter(x, y)
plt.title('Spline Interpolation')
plt.xlabel('x')
plt.ylabel('S(x)')
plt.show()
