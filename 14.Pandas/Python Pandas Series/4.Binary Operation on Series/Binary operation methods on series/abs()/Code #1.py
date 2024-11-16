# importing pandas module
import pandas as pd

# creating lists
lst = [2, -10.87, -3.14, 0.12]
lst2 = [-10.87 + 4j]

ser = pd.Series(lst)
ser1 = pd.Series(lst2)

# printing values explaining abs()
print(ser1.abs(), '\n\n', ser.abs())
