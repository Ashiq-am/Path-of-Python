# program to illustrate timetuple()
# method in Python


import datetime


# creating object and initializing
# it with custom date
birthDate = datetime.datetime(1999, 4, 6)


# obtaining the attributes and displaying them
print("Year: ", birthDate.timetuple()[0])
print("Month: ", birthDate.timetuple()[1])
print("Day: ", birthDate.timetuple()[2])
print("Hour: ", birthDate.timetuple()[3])
print("Minute: ", birthDate.timetuple()[4])
print("Second: ", birthDate.timetuple()[5])
print("Day of Week: ", birthDate.timetuple()[6])
print("Day of Year: ", birthDate.timetuple()[7])
print("Daylight Saving Time: ", birthDate.timetuple()[8])
