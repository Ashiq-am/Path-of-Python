# compare the results with sklearn package
weighted_mean_sq_error_sklearn = np.average(
	(data['Actual']-data['Predicted'])**2, axis=0, weights=y_weights)

weighted_mean_sq_error_sklearn
