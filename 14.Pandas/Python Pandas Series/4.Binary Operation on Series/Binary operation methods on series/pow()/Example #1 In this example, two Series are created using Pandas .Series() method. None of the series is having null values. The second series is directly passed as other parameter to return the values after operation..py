# importing pandas module
import pandas as pd

# creating first series
first =[1, 2, 5, 6, 3, 4]

# creating second series
second =[5, 3, 2, 1, 3, 2]

# making series
first = pd.Series(first)

# making series
second = pd.Series(second)

# calling .pow()
result = first.pow(second)

# display
result
