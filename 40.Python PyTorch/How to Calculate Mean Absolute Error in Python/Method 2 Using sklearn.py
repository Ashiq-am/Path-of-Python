# Python program for calculating Mean Absolute
# Error using sklearn

# import the module
from sklearn.metrics import mean_absolute_error as mae

# list of integers of actual and calculated
actual = [2, 3, 5, 5, 9]
calculated = [3, 3, 8, 7, 6]

# calculate MAE
error = mae(actual, calculated)

# display
print("Mean absolute error : " + str(error))
