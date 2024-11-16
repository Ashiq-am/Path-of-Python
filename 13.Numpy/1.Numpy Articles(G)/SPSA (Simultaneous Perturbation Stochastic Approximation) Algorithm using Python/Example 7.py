# Y is the polynomial to be approximated
X = np.linspace(0, 10, 100)
Y = 1*X**2 - 4*X + 3

noise = 3*np.random.normal(size=len(X))
Y += noise

# plot polynomial
plt.title("polynomial with noise")
plt.plot(X, Y, 'go')
plt.show()
