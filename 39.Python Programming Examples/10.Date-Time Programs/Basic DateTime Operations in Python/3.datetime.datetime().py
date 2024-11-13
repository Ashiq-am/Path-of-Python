from datetime import datetime

# now() gives current date and time
current = datetime.now()

# print combinedly
print(current)
print("\n")
print("print each term individually")

day = current.strftime("%d")

# print day
print("day:", day)

month = current.strftime("%m")

# print month
print("month:", month)

year = current.strftime("%Y")

# print year
print("year:", year)

time = current.strftime("%H:%M:%S")

# time in hour, minute and second
print("time:", time)

print("\n")
print("printing date and time together")
date_time = current.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)
print("\n")

# fetching details from timestamp
timestamp = 1615797322
date_time = datetime.fromtimestamp(timestamp)

# %c, %x and %X are used for locale's proper date and time representation
time_1 = date_time.strftime("%c")
print("first_output:", time_1)

time_2 = date_time.strftime("%x")
print("second_output:", time_2)

time_3 = date_time.strftime("%X")
print("third_output:", time_3)

print("\n")

# assigning each term manually
manual = datetime(2021, 3, 28, 23, 55, 59, 342380)
print("year =", manual.year)
print("month =", manual.month)
print("hour =", manual.hour)
print("minute =", manual.minute)
print("timestamp =", manual.timestamp())
