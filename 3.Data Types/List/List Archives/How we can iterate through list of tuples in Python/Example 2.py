# create a list of tuples with with atudent
# details
name = [('sravan', 7058, 98.45),
        ('ojaswi', 7059, 90.67),
        ('bobby', 7060, 78.90),
        ('rohith', 7081, 67.89),
        ('gnanesh', 7084, 98.01)]
l = []

# iterate using index with emumerate function
for index, tuple in enumerate(name):
    # access through index
    # by appending to list
    l.append(name[index])

# iterate through the list
for x in l:
    for y in x:
        print(y)
    print()
