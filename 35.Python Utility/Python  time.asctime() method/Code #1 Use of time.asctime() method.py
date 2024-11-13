# Python program to explain time.asctime() method

# importing time module
import time


# Convert the current time
# as returned by time.time() method
# to a time.struct_time object in UTC
# using time.gmtime() method
obj = time.gmtime()

# Print time.struct_time object
print("time.struct_time object as returned by time.gmtime() method:")
print(obj)

# Convert the time.struct_time
# object to a string of the
# form 'Day Mon Date Hour:Min:Sec Year'
# using time.asctime() method
time_str = time.asctime(obj)

# Print the time.struct_time object
# to the string of the
# form 'Day Mon Date Hour:Min:Sec Year'
print("\ntime.struct_time obj in string of the form 'Day Mon Date Hour:Min:Sec Year':")
print(time_str)


# Convert the current time
# as returned by time.time() method
# to a time.struct_time object in local time
# using time.localtime() method
obj = time.localtime()

# Print time.struct_time object
print("\ntime.struct_time object as returned by time.localtime() method:")
print(obj)

# Convert the time.struct_time
# object to a string of the
# form 'Day Mon Date Hour:Min:Sec Year'
# using time.asctime() method
time_str = time.asctime(obj)

# Print the time.struct_time object
# to the string of the
# form 'Day Mon Date Hour:Min:Sec Year'
print("\ntime.struct_time obj in string of the form 'Day Mon Date Hour:Min:Sec Year':")
print(time_str)
