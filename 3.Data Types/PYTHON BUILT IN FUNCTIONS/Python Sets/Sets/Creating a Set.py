"""Sets can be created by using the built-in set() function with an iterable object or a sequence by placing
the sequence inside curly braces, separated by ‘comma’.

Note – A set cannot have mutable elements like a list, set or dictionary, as its elements."""



# Python program to demonstrate
# Creation of Set in Python

# Creating a Set
set1 = set()
print("Intial blank Set: ")
print(set1)

# Creating a Set with
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)

# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)





"""A set contains only unique elements but at the time of set creation, multiple duplicate values can also be passed. 
Order of elements in a set is undefined and is unchangeable. 
Type of elements in a set need not be the same, various mixed up data type values can also be passed to the set."""






# Creating a Set with
# a List of Numbers
# (Having duplicate values)
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)

# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)

