# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating series 1
series1 = pd.Series([7, 5, 6, 4, 9])

# creating series 2
series2 = pd.Series([1, 2, 3, 10, 2])

# storing in new variable
# calling .dot() method
ans = series1.dot(series2)

# display
print('Dot product = {}'.format(ans))
