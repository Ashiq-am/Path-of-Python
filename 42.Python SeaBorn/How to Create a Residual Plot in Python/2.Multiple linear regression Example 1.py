# import packages and libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

# reading the csv file
data = pd.read_csv('homeprices.csv')
data

# fit multi linear regression model
multi_model = ols('price ~ area + bedrooms', data=data).fit()

# display model summary
print(multi_model.summary())

# modify figure size
fig = plt.figure(figsize=(14, 8))

# creating regression plots
fig = sm.graphics.plot_regress_exog(multi_model, 'area', fig=fig)
