# import packages
import pandas as pd
import numpy as np
import statsmodels.api as sm

# reading csv file as pandas dataframe
data = pd.read_csv('headbrain2.csv')

# independent variable
x = data['Head Size(cm^3)']

# output variable (dependent)
y = data['Brain Weight(grams)']

# adding constant
x = sm.add_constant(x)

#fit linear regression model
model = sm.OLS(y, x).fit()

#display model summary
print(model.summary())

# residual sum of squares
print(model.ssr)
