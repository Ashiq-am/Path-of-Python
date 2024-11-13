# Python3 code to demonstrate working of
# Extract indices of Present, Non Index matching Strings
# using enumerate() + zip() + list comprehension

# initializing strings
test_str1 = 'apple'
test_str2 = 'pineapple'

# printing original Strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# one-liner to solve this problem.
res = [idx for idx, (x, y) in enumerate(zip(test_str1, test_str2)) if x != y and x in test_str2]

# printing result
print("The extracted indices : " + str(res))
