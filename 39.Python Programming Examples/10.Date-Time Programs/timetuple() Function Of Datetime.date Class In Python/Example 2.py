import datetime

# creating xmas date object
xmas = datetime.datetime(2021, 12, 25)

# datetime instance's attributes
# are returned as a tuple.
xmasTimeTuple = xmas.timetuple()

# showing the object's tuples
print(xmasTimeTuple)
