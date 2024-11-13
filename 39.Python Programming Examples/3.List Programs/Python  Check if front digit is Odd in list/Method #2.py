# Python3 code to demonstrate
# Check if front digit is Odd in list
# using all() + list comprehension

# initializing list
test_list = [15, 7, 928829, 332]

# printing original list
print("The original list : " + str(test_list))

# using all() + list comprehension
# Check if front digit is Odd in list
res = all(int(str(i)[0]) % 2 for i in test_list)

# print result
print("Does each element start with odd digit ? " + str(res))
