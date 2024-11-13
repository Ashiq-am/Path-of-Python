# Python3 code to demonstrate working of
# String Weight
# Using sum()

# initializing string
test_str = 'GeeksforGeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing sum dictionary
sum_dict = {"G" : 5, "e" : 2, "k" : 10, "f" : 3,
			"s" : 15, "o" : 4, "r" : 6}

# sum() used to get summation
res = sum(sum_dict[ele] for ele in test_str)

# printing result
print("The weighted sum : " + str(res))
