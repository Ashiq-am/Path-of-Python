# Python3 code to demonstrate working of
# Combine Strings to Matrix
# Using list comprehension + zip() + split()

# initializing strings
test_str1 = "Gfg is best"
test_str2 = "1 2 3"

# printing original strings
print("The original string 1 is : " + test_str1)
print("The original string 2 is : " + test_str2)

# Combine Strings to Matrix
# Using list comprehension + zip() + split()
res = [[idx, int(j)] for idx, j in zip(test_str1.split(' '), test_str2.split(' '))]

# printing result
print("Does Matrix after construction : " + str(res))
