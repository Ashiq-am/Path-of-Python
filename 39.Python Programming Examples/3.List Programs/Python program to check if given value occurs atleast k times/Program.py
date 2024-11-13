# Python program to check if given
# value occurs atleast k times

test_list = [1, 3, 5, 5, 4, 5]

# printing original list
print("The original list is : " + str(test_list))

# value to be checked
val = 5

# initializing k
k = 3

# using sum() + list comprehension
# checking occurrences
res = 0
res = sum([1 for i in test_list if i == val]) >= k

if res == 1:
    res = True
else:
    res = False

# printing result
print("%d occur atleast %d times ? :" % (val, k) + str(res))
