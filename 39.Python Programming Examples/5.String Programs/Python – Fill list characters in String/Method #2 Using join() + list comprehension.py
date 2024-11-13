# Python3 code to demonstrate working of
# Fill list characters in String
# Using join() + list comprehension

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing fill list
fill_list = ['g', 's', 'f']

# join() used to concatenate result
# using conditionals in list comprehension
res = "".join([chr if chr in fill_list else "_"
			for chr in list(test_str)])

# printing result
print("The string after filling values : " + str(res))
