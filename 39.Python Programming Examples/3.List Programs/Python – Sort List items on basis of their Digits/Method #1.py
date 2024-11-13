# Python3 code to demonstrate working of
# Sort List by Digits
# Using map() + str() + ljust() + sorted()

# initializing list
test_list = [434, 211, 12, 54, 3]

# printing original list
print("The original list is : " + str(test_list))

# converting elements to string
temp1 = map(str, test_list)

# getting max length
max_len = max(map(len, temp1))

# performing sort operation
res = sorted(test_list, key = lambda idx : (str(idx).ljust(max_len, 'a')))

# printing result
print("List after sorting : " + str(res))
