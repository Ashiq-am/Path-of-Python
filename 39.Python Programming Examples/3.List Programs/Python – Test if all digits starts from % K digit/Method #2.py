# Python3 code to demonstrate
# Test if all digits starts from % K digit
# using all() + list comprehension

# initializing list
test_list = [65, 3, 92, 332]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# using all() + list comprehension
# Check if front digit is Odd in list
res = not all(int(str(i)[0]) % K for i in test_list)

# print result
print("Does each element start with % K digit ? " + str(res))
