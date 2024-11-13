import datetime
today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))

# prints the official format of date-time object
print(repr(today))





#str() displays today’s date in a way that the user can understand the date and time.

#repr() prints “official” representation of a date-time object (means using the “official” string representation so,
# we can reconstruct the object).
