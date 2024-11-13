# import packages
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# loading the csv file
df = pd.read_csv('headbrain1.csv')
print(df.head())

# fitting the model
df.columns = ['Head_size', 'Brain_weight']
model = smf.ols(formula='Head_size ~ Brain_weight',
				data=df).fit()

# model summary
print(model.summary())
