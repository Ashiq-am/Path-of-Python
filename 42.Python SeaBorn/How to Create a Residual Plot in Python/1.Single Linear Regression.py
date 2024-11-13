# import packages and libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

# reading the csv file
data = pd.read_csv('headbrain3.csv')

# fit simple linear regression model
linear_model = ols('Brain_weight ~ Head_size',
				data=data).fit()

# display model summary
print(linear_model.summary())

# modify figure size
fig = plt.figure(figsize=(14, 8))

# creating regression plots
fig = sm.graphics.plot_regress_exog(linear_model,
									'Head_size',
									fig=fig)
