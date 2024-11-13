from datetime import time

# time() takes hour, minutes, second,
# microsecond respectively in order
# if no parameter is passed in time() by default
# it takes 0
defaultTime = time()

print("default_hour =", defaultTime.hour)
print("default_minute =", defaultTime.minute)
print("default_second =", defaultTime.second)
print("default_microsecond =", defaultTime.microsecond)

# passing parameter in different-different ways
# hour, minute and second respectively is a default
# order
time1= time(10, 5, 25)
print("time_1 =", time1)

# assigning hour, minute and second to respective
# variables
time2= time(hour = 10, minute = 5, second = 25)
print("time_2 =", time2)

# assigning hour, minute, second and microsecond to
# respective variables
time3= time(hour=10, minute= 5, second=25, microsecond=55)
print("time_3 =", time3)
