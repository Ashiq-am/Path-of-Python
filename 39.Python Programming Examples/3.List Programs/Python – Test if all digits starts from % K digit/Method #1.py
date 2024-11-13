# Python3 code to demonstrate
# Test if all digits starts from % K digit
# using list comprehension + map()

# initializing list
test_list = [65, 3, 92, 332]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# using list comprehension + map()
# Test if all digits starts from % K digit
res = len(set( not(int(sub[0]) % K) for sub in map(str, test_list))) == 1

# print result
print("Does each element start with % K digit ? " + str(res))
