# import time from datetime
from datetime import time

# create time
x = time(5, 34, 7, 6789)

print("Actual Time:", x)

# replace hour from 5 to 10
final = x.replace(hour = 10)

print("New time after changing the hour:", final)
