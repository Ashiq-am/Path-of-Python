# import time from datetime
from datetime import time

# create time
x = time(5,34,7,6789)

print("Actual Time:", x)

# replace hour from 5 to 10
# replace minute from 34 to 11
# replace second from 7 to 1
# replace milli second from 6789 to 1234
final = x.replace(hour = 10, minute = 11,
				second = 1, microsecond = 1234)

print("New time :", final)
