# Importing numpy & scikit-learn
import numpy as np
from sklearn.model_selection import train_test_split

# Making a dummy array to represent x,y for example
# Making a array for x ranging from 0-15 then
# reshaping it to form a matrix of shape 8x2
x = np.arange(16).reshape((8, 2))

# y is just a list of 0-7 number representing
# target variable
y = range(8)

# Splitting dataset in 80-20 fashion .i.e.
# Training set is 80% of total data
# Testing set is 20% of total data
x_train, x_test, y_train, y_test = train_test_split(x, y,
													test_size=0.2,
													random_state=42)

# Testing set
print("Testing set x: ", x_test)
print("Testing set y: ", y_test)
