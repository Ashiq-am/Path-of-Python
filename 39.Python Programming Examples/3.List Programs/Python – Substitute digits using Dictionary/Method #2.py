# Python3 code to demonstrate working of
# Substitute digits using Dictionary
# Using join() + list comprehension + str() + int()

# initializing list
test_list = [45, 32, 87, 34, 21, 91]

# printing original list
print("The original list is : " + str(test_list))

# initializing digit mapping
dig_map = {1 : 4, 4 : 2, 3 : 8, 2 : 6, 7 : 5, 9 : 3, 8 : 9, 5 : 7}

# Substitute digits using Dictionary
# Using join() + list comprehension + str() + int()
res = [int(''.join([str(dig_map[int(ele)]) for ele in str(sub)])) for sub in test_list]

# printing result
print("List after Digit Substitution : " + str(res))
