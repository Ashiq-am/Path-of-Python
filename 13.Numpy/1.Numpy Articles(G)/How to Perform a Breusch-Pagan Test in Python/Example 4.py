# Importing libraries
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.compat import lzip
import statsmodels.stats.api as sms

# Creating a dataset
dataframe = pd.DataFrame({'rating': [92, 84, 87, 82,
									98, 94, 75, 80,
									83, 89],
						'points': [27, 30, 15, 26,
									27, 20, 16, 18,
									19, 20],
						'runs': [5000, 7000, 5102,
								8019, 1200, 7210,
								6200, 9214, 4012,
								3102],
						'wickets': [110, 120, 110,
									80, 90, 119,
									116, 100, 90,
									76]})

# Fit the regression model
fit = smf.ols('rating ~ points+runs+wickets', data=dataframe).fit()

# Conduct the Breusch-Pagan test
names = ['Lagrange multiplier statistic', 'p-value',
		'f-value', 'f p-value']

# Get the test result
test_result = sms.het_breuschpagan(fit.resid, fit.model.exog)

lzip(names, test_result)
