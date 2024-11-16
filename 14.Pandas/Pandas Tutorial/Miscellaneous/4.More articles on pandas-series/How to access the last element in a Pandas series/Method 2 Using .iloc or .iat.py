# importing the pandas library and time
import pandas as pd
import time
# initializing the series
ser = pd.Series(['g', 'e', 'e', 'k', 's'])

start = time.time()
print("The last element in the series using iloc is : ", ser.iloc[-1])
end = time.time()

print("Time taken by iloc : ", end-start)

start = time.time()
print("The last element in the series using iat is : ", ser.iat[-1])
end = time.time()

print("Time taken by iat : ", end-start)
