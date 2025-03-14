# Python3 program to demonstrate
# the use of sample() function .

# import random
import random


# Prints list of random items of
# length 3 from the given list.
list1 = [1, 2, 3, 4, 5, 6]
print("With list:", random.sample(list1, 3))

# Prints list of random items of
# length 4 from the given string.
string = "GeeksforGeeks"
print("With string:", random.sample(string, 4))

# Prints list of random items of
# length 4 from the given tuple.
tuple1 = ("ankit", "geeks", "computer", "science",
				"portal", "scientist", "btech")
print("With tuple:", random.sample(tuple1, 4))


# Prints list of random items of
# length 3 from the given set.
set1 = {"a", "b", "c", "d", "e"}
print("With set:", random.sample(set1, 3))
