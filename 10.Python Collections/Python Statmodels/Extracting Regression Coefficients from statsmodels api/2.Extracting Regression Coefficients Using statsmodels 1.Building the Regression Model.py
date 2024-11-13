import statsmodels.api as sm

# Add a constant to the independent variable
X = sm.add_constant(data['X'])

# Fit the Ordinary Least Squares (OLS) model
model = sm.OLS(data['y'], X)
results = model.fit()
