import datetime

# creating current date object
currentDate = datetime.datetime.today()

# datetime instance's attributes
# are returned as a tuple.
currentDateTimeTuple = currentDate.timetuple()

# showing the object's tuples
print(currentDateTimeTuple)
print()
print("Using a for loop, output the tuple values :")

for value in currentDateTimeTuple:
    print(value)
