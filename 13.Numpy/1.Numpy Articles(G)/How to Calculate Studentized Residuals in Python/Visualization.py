# Python program to draw the plot
# of stundenterized resiual

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

# Defining predictor variable values and
# studentized residuals
x = dataframe['Score']
y = result['student_resid']

# Creating a scatterplot of predictor variable
# vs studentized residuals
plt.scatter(x, y)
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel('Points')
plt.ylabel('Studentized Residuals')

# Save the plot
plt.savefig("Plot.png")
