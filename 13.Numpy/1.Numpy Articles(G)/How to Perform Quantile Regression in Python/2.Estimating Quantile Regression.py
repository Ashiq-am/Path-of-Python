# Python program to illustrate
# how to estimate quantile regression

# Importing libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

np.random.seed(0)

# Number of rows
rows = 20

# Constructing Distance column
Distance = np.random.uniform(1, 10, rows)

# Constructing Emission column
Emission = 40 + Distance + np.random.normal(loc=0,
											scale=.25*Distance,
											size=20)

# Creating the data set
df = pd.DataFrame({'Distance': Distance,
				'Emission': Emission})

# fit the model
model = smf.quantreg('Emission ~ Distance',
					df).fit(q=0.7)

# view model summary
print(model.summary())
