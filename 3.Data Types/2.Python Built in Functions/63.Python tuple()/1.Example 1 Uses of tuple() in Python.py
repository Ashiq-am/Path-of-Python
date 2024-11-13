# when parameter is not passed
tuple1 = tuple()
print("empty tuple:", tuple1)

# when an iterable(e.g., list) is passed
list1= [ 1, 2, 3, 4 ]
tuple2 = tuple(list1)
print("list to tuple:", tuple2)

# when an iterable(e.g., dictionary) is passed
dict = { 1 : 'one', 2 : 'two' }
tuple3 = tuple(dict)
print("dict to tuple:", tuple3)

# when an iterable(e.g., string) is passed
string = "geeksforgeeks";
tuple4 = tuple(string)
print("str to tuple:", tuple4)
