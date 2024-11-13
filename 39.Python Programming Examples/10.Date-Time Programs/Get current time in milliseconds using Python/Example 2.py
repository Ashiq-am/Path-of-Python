# Python program to get
# time in milliseconds


# Import class time from time module
from time import time

# Get time in milliseconds using
# lambda function
milliseconds = lambda: int(time() * 1000)

print("Time in milliseconds since epoch", milliseconds())
