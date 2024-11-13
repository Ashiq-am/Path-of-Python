# Python3 code to demonstrate working of
# Similar other index element if K
# Using list comprehension + zip()

# initializing list
test_list = [5, 7, 3, 2, 3, 8, 6]

# printing original list
print("The original list : " + str(test_list))

# initializing arg. list
arg_list = [4, 5, 8, 3, 7, 9, 3]

# initializing K
K = 3

# Using zip() to lock both the lists, with similar indices mapping
res = [ele for ele, ele1 in zip(arg_list, test_list) if ele1 == K]

# printing result
print("Extracted elements : " + str(res))
