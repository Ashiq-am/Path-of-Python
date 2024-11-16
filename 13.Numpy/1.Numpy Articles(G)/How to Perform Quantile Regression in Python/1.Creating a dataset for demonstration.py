# Python program to create a dataset

# Importing libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

np.random.seed(0)

# Specifying the number of rows
rows = 20

# Constructing Distance column
Distance = np.random.uniform(1, 10, rows)

# Constructing Emission column
Emission = 20 + np.random.normal(loc=0, scale=.25*Distance, size=20)

# Creating a dataframe
df = pd.DataFrame({'Distance': Distance, 'Emission': Emission})

df.head()
