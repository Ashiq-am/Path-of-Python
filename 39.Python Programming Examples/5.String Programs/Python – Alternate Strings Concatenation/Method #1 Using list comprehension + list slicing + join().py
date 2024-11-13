# Python3 code to demonstrate
# Alternate Strings Concatenation
# using list comprehension + list slicing

# initializing list
test_list = ["GFG", "is", "for", "Computer", "Science", "learning"]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + list slicing
# Alternate Strings Concatenation
res = [" ".join(test_list[i : : 2]) for i in range(len(test_list) //
												(len(test_list)//2))]

# print result
print("The alternate elements concatenation list : " + str(res))
