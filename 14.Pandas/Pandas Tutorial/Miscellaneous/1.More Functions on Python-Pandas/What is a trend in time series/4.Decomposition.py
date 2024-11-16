# importing function
from statsmodels.tsa.seasonal import seasonal_decompose

# creating trend object by assuming multiplicative model
output = seasonal_decompose(data, model='multiplicative').trend

# creating plot
output.plot()
