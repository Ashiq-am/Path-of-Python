# import time from datetime
from datetime import time

# create time
x = time(5,34,7,6789)

print("Actual Time:", x)

# replace second from 7 to 2
final = x.replace(second = 2)

print("New time after changing the second:", final)
