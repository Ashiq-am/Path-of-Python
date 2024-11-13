# Python3 code to demonstrate working of
# Characters Positional Summation in String List
# Using list comprehension + sum() + ord()

# initializing list
test_list = ["geeksforgeeks", "teaches",
			"us", "discipline"]

# printing original list
print("The original list is : " + str(test_list))

# sum() gets summation, list comprehension
# used to perform task in one line
res = [sum([ord(ele) - 96 for ele in sub]) for sub in test_list]

# printing result
print("Positional Summation List : " + str(res))
