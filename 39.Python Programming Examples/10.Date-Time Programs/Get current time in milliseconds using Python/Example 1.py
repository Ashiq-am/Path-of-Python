# Python program to get
# time in milliseconds

# Import class time from time module
from time import time

# time() function is multiplied with
# 1000 to convert seconds into milliseconds.
milliseconds = int(time() * 1000)

print("Time in milliseconds since epoch", milliseconds)
