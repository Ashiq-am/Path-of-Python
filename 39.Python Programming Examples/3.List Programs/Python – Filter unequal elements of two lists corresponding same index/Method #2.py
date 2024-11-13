# Python3 code to demonstrate working of
# Unequal Equi-index elements
# using list comprehension + zip()

# initialize lists
test_list1 = ["a", "b", "c", "d"]
test_list2 = ["g", "b", "s", "d"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Unequal Equi-index elements
# using list comprehension + zip()
res = [i for i, j in zip(test_list1, test_list2) if i != j]

# printing result
print("Unequal index elements in lists : " + str(res))
