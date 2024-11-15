# Python3 program demonstrating
# the use of tuple() function

# when parameter is not passed
tuple1 = tuple()
print(tuple1)

# when an iterable(e.g., list) is passed
list1= [ 1, 2, 3, 4 ]
tuple2 = tuple(list1)
print(tuple2)

# when an iterable(e.g., dictionary) is passed
dict = { 1 : 'one', 2 : 'two' }
tuple3 = tuple(dict)
print(tuple3)

# when an iterable(e.g., string) is passed
string = "geeksforgeeks"
tuple4 = tuple(string)
print(tuple4)
