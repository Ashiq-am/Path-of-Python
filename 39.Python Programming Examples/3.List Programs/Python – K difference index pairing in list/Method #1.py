# Python3 code to demonstrate working of
# K difference index pairing in list
# using list comprehension + zip()

# initialize list
test_list = ["G", "F", "G", "I", "S", "B", "E", "S", "T"]

# printing original list
print("The original list : " + str(test_list))

# initialize K
K = 3

# K difference index pairing in list
# using list comprehension + zip()
res = [i + j for i, j in zip(test_list, test_list[K :])]

# printing result
print("List after K difference concatenation is : " + str(res))
