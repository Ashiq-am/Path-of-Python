from scipy.interpolate import UnivariateSpline

# Sample noisy data
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + np.random.normal(0, .1, x.size)

# Fit smoothing spline
spl = UnivariateSpline(x, y)

# Plotting
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'r', lw=2)
plt.scatter(x,y)
plt.title('Smoothing Spline')
plt.xlabel('x')
plt.ylabel('S(x)')
plt.show()
