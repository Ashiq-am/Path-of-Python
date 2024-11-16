import pandas as pd
import numpy as np
import random

# create a dataset with actual and
# predicted values
d = {'Actual': np.arange(0, 20, 2)*np.sin(2),
	'Predicted': np.arange(0, 20, 2)*np.cos(2)}

# convert the data to pandas dataframe
data = pd.DataFrame(data=d)

# create a weights array based on
# the importance
y_weights = np.arange(2, 4, 0.2)

# calculate the squared difference
diff = (data['Actual']-data['Predicted'])**2

# compute the weighted mean square error
weighted_mean_sq_error = np.sum(diff * y_weights) / np.sum(y_weights)
