# Python program to calculate studenterized residual

# Importing necessary packages
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

# Creating dataframe
dataframe = pd.DataFrame({'Score': [80, 95, 80, 78, 84,
									96, 86, 75, 97, 89],
				'Benchmark': [27, 28, 18, 18, 29, 30,
								25, 25, 24, 29]})

# Building simple linear regression model
simple_regression_model = ols('Score ~ Benchmark', data=dataframe).fit()

# Producing studenterized residual
result = simple_regression_model.outlier_test()

print(result)
