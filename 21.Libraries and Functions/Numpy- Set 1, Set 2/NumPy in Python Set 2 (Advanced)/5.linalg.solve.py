
import numpy as np

# coefficients
a = np.array([[1, 2], [3, 4]])
# constants
b = np.array([8, 18])

print("Solution of linear equations:", np.linalg.solve(a, b))










"""Finally, we see an example which shows how one can perform linear regression using least squares method.

A linear regression line is of the form w1x + w2 = y and it is the line that minimizes the sum of the squares 
of the distance from each data point to the line. 
So, given n pairs of data (xi, yi), the parameters that we are looking for are w1 and w2 which minimize the error:"""