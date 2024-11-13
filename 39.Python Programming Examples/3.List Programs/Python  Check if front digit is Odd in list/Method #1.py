# Python3 code to demonstrate
# Check if front digit is Odd in list
# using list comprehension + map()

# initializing list
test_list = [15, 7, 928829, 332]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + map()
# Check if front digit is Odd in list
res = len(set( not(int(sub[0]) % 2) for sub in map(str, test_list))) == 1

# print result
print("Does each element start with odd digit ? " + str(res))
