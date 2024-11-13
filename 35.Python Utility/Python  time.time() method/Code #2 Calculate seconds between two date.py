# Python program to explain time.time() method

# importing time module
import time

# Date 1
date1 = "1 Jan 2000 00:00:00"

# Date 2
# Current date
date2 = "22 Aug 2019 00:00:00"

# Parse the date strings
# and convert it in
# time.struct_time object using
# time.strptime() method
obj1 = time.strptime(date1, "% d % b % Y % H:% M:% S")
obj2 = time.strptime(date2, "% d % b % Y % H:% M:% S")

# Get the time in seconds
# since the epoch
# for both time.struct_time objects
time1 = time.mktime(obj1)
time2 = time.mktime(obj2)

print("Date 1:", time.asctime(obj1))
print("Date 2:", time.asctime(obj2))


# Seconds between Date 1 and date 2
seconds = time2 - time1
print("Seconds between date 1 and date 2 is % f seconds" % seconds)
