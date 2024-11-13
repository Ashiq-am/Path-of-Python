# Python code to demonstrate
# the working of cmp()
# only integer case.

# initializing argument lists
from filecmp import cmp

list1 = [ 1, 2, 4, 3]
list2 = [ 1, 2, 5, 8]
list3 = [ 1, 2, 5, 8, 10]
list4 = [ 1, 2, 4, 3]

# Comparing lists
print("Comparison of list2 with list1 : ",)
print(cmp(list2, list1))

# prints -1, because list3 has larger size than list2
print("Comparison of list2 with list3(larger size) : ",)
print(cmp(list2, list3))

# prints 0 as list1 and list4 are equal
print("Comparison of list4 with list1(equal) : ",)
print(cmp(list4, list1))
