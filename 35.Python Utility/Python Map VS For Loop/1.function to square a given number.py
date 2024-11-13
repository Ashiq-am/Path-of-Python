# function to square a given number
def squareNum (a) :
	return a * a


listt = [0, -1, 3, 4.5, 99, .08]

# using 'map' to call the function
# 'squareNum' for all the elements
# of 'listt'
x = map(squareNum, listt)

# map function returns a map
# object at this particular
# location
print(x)

# convert map to list
print(list(x))


# alternate way to square all
# elements of 'listt' using
# 'for loop'

for i in listt :
	square = i * i
	print(square)
