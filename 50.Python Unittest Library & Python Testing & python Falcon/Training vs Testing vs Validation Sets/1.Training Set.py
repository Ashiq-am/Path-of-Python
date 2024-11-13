# Importing numpy & scikit-learn
import numpy as np
from sklearn.model_selection import train_test_split

# Making a dummy array to
# represent x,y for example
# Making a array for x ranging
# from 0-15 then reshaping it
# to form a matrix of shape 8x2
x = np.arange(16).reshape((8,2))

# y is just a list of 0-7 number
# representing target variable
y = range(8)

# Splitting dataset in 80-20 fashion .i.e.
# Testing set is 20% of total data
# Training set is 80% of total data
x_train, x_test, y_train, y_test = train_test_split(x,y,
													train_size=0.8,
													random_state=42)

# Training set
print("Training set x: ",x_train)
print("Training set y: ",y_train)
