# Python3 code to demonstrate working of
# Convert Lists to Nestings Dictionary
# Using list comprehension + zip()

# initializing list
test_list1 = ["gfg", 'is', 'best']
test_list2 = ['ratings', 'price', 'score']
test_list3 = [5, 6, 7]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
print("The original list 3 is : " + str(test_list3))

# Convert Lists to Nestings Dictionary
# Using list comprehension + zip()
res = [{a: {b: c}} for (a, b, c) in zip(test_list1, test_list2, test_list3)]

# printing result
print("The constructed dictionary : " + str(res))
