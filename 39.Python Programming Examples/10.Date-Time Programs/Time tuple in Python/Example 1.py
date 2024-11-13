# program to illustrate timetuple()
# method in Python


import datetime


# creating object
obj = datetime.datetime.today()

# obtaining the attributes of the
# datetime instance as a tuple
objTimeTuple = obj.timetuple()

# displaying the tuples of the object
print(objTimeTuple)
