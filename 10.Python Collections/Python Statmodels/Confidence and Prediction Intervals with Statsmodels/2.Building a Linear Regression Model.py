# Generate synthetic data
np.random.seed(0)
n = 100
x = np.linspace(0, 10, n)
e = np.random.normal(size=n)
y = 1 + 0.5 * x + 2 * e

# Add a constant term for the intercept
X = sm.add_constant(x)

# Fit the OLS model
model = sm.OLS(y, X).fit()
print(model.summary())
