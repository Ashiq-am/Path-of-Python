# Python3 code to demonstrate working of
# Convert Joint Float string to Numbers
# Using list comprehension + float()

# initializing string
test_str = "45.6778.4524.45"

# printing original string
print("The original string is : " + test_str)

# Convert Joint Float string to Numbers
# Using list comprehension + float()
res = [float(test_str[idx : idx + 5]) for idx in range(0, len(test_str), 5)]

# printing result
print("The float list is : " + str(res))
