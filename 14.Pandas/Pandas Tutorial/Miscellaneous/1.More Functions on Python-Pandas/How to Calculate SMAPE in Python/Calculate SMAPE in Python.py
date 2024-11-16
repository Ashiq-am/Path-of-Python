import pandas as pd
import numpy as np

# Define the function to return the SMAPE value
def calculate_smape(actual, predicted) -> float:

	# Convert actual and predicted to numpy
	# array data type if not already
	if not all([isinstance(actual, np.ndarray),
				isinstance(predicted, np.ndarray)]):
		actual, predicted = np.array(actual),
		np.array(predicted)

	return round(
		np.mean(
			np.abs(predicted - actual) /
			((np.abs(predicted) + np.abs(actual))/2)
		)*100, 2
	)


if __name__ == '__main__':

	# CALCULATE SMAPE FROM PYTHON LIST

	actual = [136, 120, 138, 155, 149]
	predicted = [134, 124, 132, 141, 149]

	# Get SMAPE for python list as parameters
	print("py list :",
		calculate_smape(actual, predicted), "%")

	# CALCULATE SMAPE FROM NUMPY ARRAY
	actual = np.array([136, 120, 138, 155, 149])
	predicted = np.array([134, 124, 132, 141, 149])

	# Get SMAPE for python list as parameters
	print("np array :",
		calculate_smape(actual, predicted), "%")

	# CALCULATE SMAPE FROM PANDAS DATAFRAME
	# Define the pandas dataframe
	sales_df = pd.DataFrame({
		"actual" : [136, 120, 138, 155, 149],
		"predicted" : [134, 124, 132, 141, 149]
	})

	# Get SMAPE for pandas series as parameters
	print("pandas df:", calculate_smape(sales_df.actual,
										sales_df.predicted), "%")
