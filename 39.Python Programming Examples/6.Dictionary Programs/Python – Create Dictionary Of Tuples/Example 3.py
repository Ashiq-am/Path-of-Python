# one value is age of student
# second value is student name
data = ((24, "bobby"), (21, "ojsawi"))

# convert into dictionary
final = dict((value, key) for key, value in data)

# display
print(final)
