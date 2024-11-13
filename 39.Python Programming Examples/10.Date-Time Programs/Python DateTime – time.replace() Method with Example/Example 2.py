# import time from datetime
from datetime import time

# create time
x = time(5, 34, 7, 6789)

print("Actual Time:", x)

# replace minute from 34 to 12
final = x.replace(minute = 12)

print("New time after changing the minute:", final)
