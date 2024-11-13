# Python3 code to demonstrate
# K length Padding in List
# using list comprehension

# initializing list
test_list = [3, 54, 4, 100, 10]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 4

# using list comprehension
# K length Padding in List
temp = "% 0" + str(K) + "d"
res = [temp % i for i in test_list]

# printing result
print ("The list after K size element padding : " + str(res))
