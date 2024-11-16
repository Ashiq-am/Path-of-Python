# importing the pandas library
import pandas as pd
# initializing the series
ser = pd.Series(['g', 'e', 'e', 'k', 's'])

# printing the last element using tail
print("The last element in the series using tail is : ", ser.tail(1).item())
