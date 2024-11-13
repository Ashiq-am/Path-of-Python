import sys

# sample lists
list1 = [1, 2, 3, 5]
list2 = ["GeeksForGeeks", "Data Structure", "Algorithms"]
list3 = [1, "Geeks", 2, "For", 3, "Geeks"]

# print the sizes of sample lists
print("Size of list1: " + str(sys.getsizeof(list1)) + "bytes")
print("Size of list2: " + str(sys.getsizeof(list2)) + "bytes")
print("Size of list3: " + str(sys.getsizeof(list3)) + "bytes")
