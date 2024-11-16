# import packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# reading csv file as pandas dataframe
data = pd.read_csv('headbrain2.csv')

# independent variable
X = data[['Head Size(cm^3)']]

# output variable (dependent)
y = data['Brain Weight(grams)']

# using the linear regression model
model = LinearRegression()

# fitting the data
model.fit(X, y)

# predicting values
y_pred = model.predict(X)
df = pd.DataFrame({'Actual': y, 'Predicted':
y_pred})

print(' residual sum of squares is : '+ str(np.sum(np.square(df['Predicted'] - df['Actual']))))
