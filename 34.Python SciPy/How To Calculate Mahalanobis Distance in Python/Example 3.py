# Importing libraries

import numpy as np
import pandas as pd
import scipy as stats

# calculateMahalanobis function to calculate
# the Mahalanobis distance
def calculateMahalanobis(y=None, data=None, cov=None):

	y_mu = y - np.mean(data)
	if not cov:
		cov = np.cov(data.values.T)
	inv_covmat = np.linalg.inv(cov)
	left = np.dot(y_mu, inv_covmat)
	mahal = np.dot(left, y_mu.T)
	return mahal.diagonal()

# create new column in dataframe that contains
# Mahalanobis distance for each row
df['calculateMahalanobis'] = mahalanobis(x=df, data=df[['Price', 'Distance',
														'Emission','Performance',
														'Mileage']])
