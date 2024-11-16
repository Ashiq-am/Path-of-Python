# Importing numpy & scikit-learn
import numpy as np
from sklearn.model_selection import train_test_split

# Making a dummy array to represent x,y for example
# Making a array for x ranging from 0-23 then reshaping it
# to form a matrix of shape 8x3
x = np.arange(24).reshape((8,3))

# y is just a list of 0-7 number representing
# target variable
y = range(8)

# Splitting dataset in 80-20 fashion .i.e.
# Training set is 80% of total data
# Combined set of testing & validation is
# 20% of total data
x_train, x_Combine, y_train, y_Combine = train_test_split(x,y,
											train_size=0.8,
											random_state=42)

# Splitting combined dataset in 50-50 fashion .i.e.
# Testing set is 50% of combined dataset
# Validation set is 50% of combined dataset
x_val, x_test, y_val, y_test = train_test_split(x_Combine,
												y_Combine,
												test_size=0.5,
												random_state=42)

# Training set
print("Training set x: ",x_train)
print("Training set y: ",y_train)
print(" ")

# Testing set
print("Testing set x: ",x_test)
print("Testing set y: ",y_test)
print(" ")

# Validation set
print("Validation set x: ",x_val)
print("Validation set y: ",y_val)
