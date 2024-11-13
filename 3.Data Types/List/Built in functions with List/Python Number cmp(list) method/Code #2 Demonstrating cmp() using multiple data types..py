# Python code to demonstrate
# the working of cmp()
# multiple data types

# initializing argument lists
from filecmp import cmp

list1 = [ 1, 2, 4, 10]
list2 = [ 1, 2, 4, 'a']
list3 = [ 'a', 'b', 'c']
list4 = [ 'a', 'c', 'b']


# Comparing lists
# prints 1 because string
# at end compared to number
# string is greater
print("Comparison of list2 with list1 : ",)
print(cmp(list2, list1))

# prints -1, because list3
# has an alphabet at beginning
# even though size of list2
# is greater, Comparison
# is terminated at 1st
# element itself.
print("Comparison of list2 with list3(larger size) : ",)
print(cmp(list2, list3))

# prints -1 as list4 is greater than
# list3
print("Comparison of list3 with list4 : ",)
print(cmp(list3, list4))
